<!--
author: Volker Göhler
version: 0.2.0
comment: This repository is a collection of Safety Signs for the DiAgnostiK Project
@import: https://github.com/Ifi-DiAgnostiK-Project/Piktogramme/blob/main/makros.md?raw=true


-->

# Badges

![Update makros.md on push](https://github.com/Ifi-DiAgnostiK-Project/Piktogramme/actions/workflows/github_workflows_update-makros.yml/badge.svg)

[![LiaScript Course](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/Ifi-DiAgnostiK-Project/Piktogramme/blob/main/README.md?raw=true)

[![LiaScript LiveEditor](https://raw.githubusercontent.com/LiaScript/LiaScript/refs/heads/development/badges/editor.svg)](https://liascript.github.io/LiveEditor/?/show/file/https://github.com/Ifi-DiAgnostiK-Project/Piktogramme/blob/main/README.md?raw=true)

[![GitHub](https://img.shields.io/badge/Ansehen%20auf-GitHub-181717?logo=github)](https://github.com/Ifi-DiAgnostiK-Project/Piktogramme/blob/main/README.md)

# DiAgnostiK Piktogramme
Repository für unsere Sicherheitszeichen nach ISO 7010.

- Link zur LiaScript [Bildhilfe](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/docs/master/README.md#24)! 😃

Das  LiaScript Dokument muss mit einem Kommentar beginnen indem die Makro Datei eingefügt wird. Das kann auch in dieser Datei beobachtet werden.

```markdown
<!--
@import: https://github.com/Ifi-DiAgnostiK-Project/Bildersammlung/vgoehler/Piktogramme/blob/main/makros.md?raw=true
-->
```

## Beispiel

Alle Beispiele funktionieren nur mit LiaScript und nicht hier im Github! Bitte obigen Link zu Kurs oder Live Editor nutzen.

### einfach mit Makro:

> `@Brandschutzzeichen.Richtungspfeil_Rechts(10)`

@Brandschutzzeichen.Richtungspfeil_Rechts(10)

- aber Achtung Deutsche Umlaute sind ausgeschrieben! (ä=ae usw.)

### schwieriger direkt als markdown Bild

- funktioniert auch außerhalb von LiaScript!

```md
![Beispielzeichen](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/Brandschutzzeichen/Sicherheitszeichen_Brandschutz_Richtungspfeil_Rechts.jpg?raw=true)
```

![Beispielzeichen](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/img/Brandschutzzeichen/Richtungspfeil_Rechts.jpg?raw=true)<!-- style="height: 10rem;" -->

### Skalierung

Der Parameter (die Zahl in den runden Klammern) steuert die Größe in Zeilenhöhe des Textes.

> `@Gebotszeichen.Gehoerschutz(10)`
@Gebotszeichen.Gehoerschutz(10)

> `@Gebotszeichen.Warnweste(5)`
@Gebotszeichen.Warnweste(5)

> `@Gebotszeichen.Uebergang(1)`
@Gebotszeichen.Uebergang(1)

## Bildermakros

Alle Bilder sind in dieser Datei abgebildet:

- [makros.md](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/makros.md)

Zum anzeigen bitte folgenden LiaScript Link benutzen:

[![LiaScript Course](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/makros.md?raw=true)
