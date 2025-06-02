import os

ignore_dirs = ['Collections']

makros_setup = '''<!--
author: Volker Göhler, Niklas Werner
email: volker.goehler@informatik.tu-freiberg
version: 0.2.0
repository: https://github.com/vgoehler/DiAgnostiK_Bilder_Test 

@diagnostik_image
    <img 
        src="https://raw.githubusercontent.com/vgoehler/DiAgnostiK_Bilder_Test/refs/heads/main/img/@0/@1"
        alt="@1"
        style="height: @2rem"
    >
@end
'''

location = 'https://raw.githubusercontent.com/vgoehler/DiAgnostiK_Bilder_Test/refs/heads/main/makros.md'

how_to_use = f'''
# Link zu LiaScript

[![LiaScript Course](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?{location})

[![LiaScript LiveEditor](https://raw.githubusercontent.com/LiaScript/LiaScript/refs/heads/development/badges/editor.svg)](https://liascript.github.io/LiveEditor/?/show/file/{location})



> Diese Datei ist automatisch generiert und enthält Makros für die DiAgnostiK-Bilder.

# Anleitung

Der Befehl zum einbinden eines Bildes lautet `@<Bereich>.<Name>(Größe)`
Der Bereich ist der Ordnername, in dem sich das Bild befindet.
Der Name ist der Dateiname ohne Endung.
Alle Bereiche und Befehle um alle Bilder zu laden sind in den Tabellen weiter unten abgebildet.
Die Größe ist in Zeilen angegeben, die das Bild hoch sein soll.
Die Anzeige benötigt LiaScript!

## Beispiel:

@Brandschutzzeichen.Brandbekämpfung(10)

`@Brandschutzzeichen.Brandbekämpfung(10)`

## Bereiche und Befehle
'''

def process_folders(base_path):
    img_path = os.path.join(base_path, 'img')
    makros = [makros_setup]
    showcase = [how_to_use]

    for entry in os.listdir(img_path):
        full_path = os.path.join(img_path, entry)

        if os.path.isdir(full_path) and entry not in ignore_dirs:
            showcase.append(f"\n### {entry}\n\n|Bild|Name|Befehl|\n|---|---|---|\n")
            process_file(full_path, makros, showcase)

    makros.append("\n-->\n")

    return makros + showcase

def process_file(parent_folder, makros, showcase):
    """This writes a makro and a showcase for all files in a given folder."""
    for item in os.listdir(parent_folder):
        filename = item.split('.')[0]
        entry = os.path.basename(parent_folder)
        makros.append(f'\n@{entry}.{filename}\n    @diagnostik_image({entry},{item},@0)\n@end\n')
        showcase.append(f"|@{entry}.{filename}(10)|`{item}`|`@{entry}.{filename}(10)`\n")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    text = process_folders(current_dir)
    makros_path = os.path.join(current_dir, "makros.md")
    with open(makros_path, "w", encoding="utf-8") as f:
        f.write("\n".join(text))
