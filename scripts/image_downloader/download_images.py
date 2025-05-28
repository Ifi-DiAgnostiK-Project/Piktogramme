import os
import re
import requests
from bs4 import BeautifulSoup
import argparse
from urllib.parse import urlparse


def sanitize_name(name):
    """
    Sanitizes a string to make it safe for use as a file or folder name by removing invalid characters.
    Specifically allows German Umlaute (ÄÖÜäöü) and ß in addition to letters, digits, underscores, and dots.

    :param name: The original string to sanitize.
    :return: A sanitized string with invalid characters replaced by underscores.
    """
    return re.sub(r"[^a-zA-Z0-9ÄÖÜäöüß_.]", "_", name)

def get_file_extension(url, default_ext=".jpg"):
    """
    Extract the file extension from a URL. If no valid extension is found, return a default extension.

    :param url: The URL of the file (e.g., an image URL).
    :param default_ext: The default extension to use if no extension is found in the URL.
    :return: The file extension (e.g., '.jpg', '.png').
    """
    parsed_url = urlparse(url)
    _, ext = os.path.splitext(parsed_url.path)  # Split the path into root and extension

    # Return the extracted extension, or fall back to the default
    return ext if ext else default_ext

def download_images(start_folder="."):
    """
    Downloads images from links in markdown files, creating folders based on link names,
    and naming images based on their alt tags.
    """

    for filename in os.listdir(start_folder):
        if filename.endswith(".md"):
            filepath = os.path.join(start_folder, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                markdown_content = f.read()

            # Extract the link from the markdown file
            match = re.search(r"\[(.*?)\]\((.*?)\)", markdown_content)
            if not match:
                print(f"No link found in {filename}")
                continue

            desc, link = match.groups()

            # Create a folder based on the link name (remove invalid characters)
            folder_name = os.path.join(start_folder, sanitize_name(desc))
            os.makedirs(folder_name, exist_ok=True)

            try:
                response = requests.get(link)
                response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

                soup = BeautifulSoup(response.content, "html.parser")
                img_tags = soup.find_all("img")

                for img in img_tags:
                    alt_text = img.get("alt")
                    img_url = img.get("src")

                    if not img_url:
                        print(f"Skipping image with no src attribute in {link}")
                        continue
                    
                    # Handle relative URLs
                    if not img_url.startswith("http"):
                        from urllib.parse import urljoin
                        img_url = urljoin(link, img_url)

                    if alt_text:
                        ext = get_file_extension(img_url)
                        filename = sanitize_name(alt_text) + ext
                        filepath = os.path.join(folder_name, filename)

                        try:
                            img_response = requests.get(img_url, stream=True)
                            img_response.raise_for_status()

                            with open(filepath, "wb") as f:
                                for chunk in img_response.iter_content(chunk_size=8192):
                                    f.write(chunk)

                            print(f"Downloaded: {filename} from {link}")

                        except requests.exceptions.RequestException as e:
                            print(f"Error downloading image from {img_url}: {e}")
                    else:
                        print(f"Skipping image with no alt text in {link}")

            except requests.exceptions.RequestException as e:
                print(f"Error accessing {link}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automatic Image Downloader")
    parser.add_argument("start_folder", nargs="?", default=".", help="The folder containing the markdown files.")
    args = parser.parse_args()

    download_images(args.start_folder)

