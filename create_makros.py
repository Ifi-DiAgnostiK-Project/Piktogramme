import os

ignore_dirs = ['Collections']

makros_setup = '''<!--
@diagnostik_image
    <img 
        src="https://raw.githubusercontent.com/vgoehler/DiAgnostiK_Bilder_Test/refs/heads/main/@0/@1"
        alt="@1"
        style="height: @2rem"
    >
@end
'''

how_to_use = '''

# How to

Der Befehl zum einbinden eines Bilds lautet `@Überschrift(Name, Größe)`

Die Überschrift steht über der Tabelle, der Name darin neben dem Bild.
Die Größe ist in Zeilen angegeben, die das Bild hoch sein soll.


Beispiel:

@Brandschutzzeichen(Brandbekämpfung.jpg, 10)

`@Brandschutzzeichen(Brandbekämpfung.jpg, 10)`

'''

def get_folders_and_contents(base_path):
    img_path = os.path.join(base_path, 'img')
    makros = makros_setup
    showcase = how_to_use

    for entry in os.listdir(img_path):
        full_path = os.path.join(img_path, entry)

        if os.path.isdir(full_path) and entry not in ignore_dirs:
            makros += f'\n@{entry}\n    @diagnostik_image({entry},@0,@1)\n@end\n'

            showcase += f"\n## {entry}\n\n|Bild|Name|\n|---|---|\n"

            for item in os.listdir(full_path):
                showcase += f"|@{entry}({item}, 10)|`{item}`|\n"

    makros += "\n-->\n"

    return makros + showcase

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    text = get_folders_and_contents(current_dir)
    makros_path = os.path.join(current_dir, "makros.md")
    with open(makros_path, "w", encoding="utf-8") as f:
        f.write(text)