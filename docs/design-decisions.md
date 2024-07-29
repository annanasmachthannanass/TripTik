---
title: Design Decisions
nav_order: 3
---

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Frontend Design Method

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 23.06.2024

### Problem statement

Wir möchten, dass unsere Webseite ein bestimmtes Aussehen hat, um so auch die Funktionalitäten optimal zu gewährleisten. 
Wir wollten so früh wie möglich beginnen, damit es am Ende keinen Zeitdruck gibt.

Entscheidung getroffen von: Eliana Kaping, Rojin Aylin Aslan, Johanna Engels

### Decision

Wir haben uns dafür entschieden, mit CSS zu arbeiten. 
Aus früheren Semestern kennen wir die grundlegende Struktur und Möglichkeiten davon. Dies hat es uns ermöglicht, auch schon vor der Vorlesung zum Thema User-Interface mit dem Projekt zu beginnen. Zudem lernen wir dieses Semester in diesem und auch anderen Kursen viele verschiedene neue Technologien kennen und konzentrieren uns daher lieber auf andere, die notwendiger sind wie Python und Flask.

### Regarded options

Wir haben zwischen CSS und Bootstrap überlegt.

| Criterion | CSS | Bootstrap |
| --- | --- | --- |
| **Know-how** | ✔️ Wir kennen die grundlegende Funktionsweise und Gestaltungsmöglichkeiten | ❌ Wir müssen uns mit der Implementierung, Verwendung und Gestaltung von vorne befassen |
| **Aussehen anpassen** | ❌ Alles muss grundlegend von vorne aufgebaut werden | ❔ Good: Es gibt schon eine große Anzahl an Vorlagen und Klassen, die einfach verwendet werden können, Bad: Man muss alles ausprobieren und testen, was welche Änderungen bewirkt |
| **Verwendung** | ✔️ Kann einfach verwendet werden, Datei muss nur in der html-Datei verlinkt sein -> kann so auch leicht gewechselt werden | ❌ Muss erst installiert und in das Projekt eingebunden werden | 

---

## 02: Verwendung von JavaScript

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 23.06.2024

### Problem statement

Wir möchten, dass beim Erstellen der Reise die ausgewählten Bilder direkt angezeigt werden, um das Nutzererlebnis zu verbessern indem der Nutzer sie nochmals kontrollieren kann.

Entscheidung getroffen von: Eliana Kaping, Rojin Aylin Aslan, Johanna Engels

### Decision

Wir haben uns dafür entschieden, dafür JavaScript zu verwenden.
Dies bietet die Möglichkeit, gleich auf der Clientseite die Bilder anzunehmen und sofort wieder anzuzeigen ohne die Notwendigkeit einer sofortigen Verarbeitung im Server.

### Regarded options

Wir haben zwischen JavaScript und einer serverseitigen Verarbeitung überlegt.

Es gibt verschiedene Möglichkeiten, um unser Problem umzusetzen. Da es sich dabei um einen eher kleinen Teil unseres Projektes handelt, der auch nicht elementar wichtig für die Funktionalität ist, haben wir nach einer schnellen und einfachen Lösung gesucht. Mithilfe von ChatGPT und der Erklärung einiger Online-Tutorials war dies mit JavaSript gegeben. Wir mussten noch keine fertige Projektstruktur haben oder uns ausführlich mit der Funktionsweise von Flask und Python für diese kleine Aufgabe auseinandersetzen. Es reicht, ein kleines Script-Tag in die html-Datei selbst zu schreiben. Dies haben wir viel mit ChatGPT entwickelt, da wir uns so auch nicht erst mit den genauen Funktionsweisen von JavaScript beschäftigen mussten. 

---

## 03: Datenbanklösung

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 23.06.2024

### Problem statement

Wir brauchen eine Datenbank, um die Nutzerprofile mit Username, Passwort und den Reisen zu speichern. 
Dafür benötigen wir eine Lösung, die sich gut in unser Projekt mit Python und Flask einbauen lässt.

Entscheidung getroffen von: Eliana Kaping, Rojin Aylin Aslan, Johanna Engels

### Decision

Wir haben uns dafür entschieden, eine SQLite Datenbank zu verwenden. 
Dies ist bereits im Python Paket enthalten und benötigt keine externe Anbindung. Wir kennen bereits den Oracle-Dialekt von SQL, sind also schon mit den Grundbegriffen und Funktonalitäten bekannt. Zudem ist die Datenbank so leichtgewichtig und kann einfach in unser Projekt mit eingebaut werden. 

### Regarded options

| Criterion | SQLite | Firebase |
| --- | --- | --- |
| **Know-how** | ✔️ Wir sind Vertraut mit SQL und der Nutzung von SQLite, da es im Python-Paket enthalten ist und mit Oracle SQL vergleichbar ist. | ❌ Mangelndes Wissen über NoSQL-Datenbanken und Firebase-spezifische APIs. Erfordert zusätzliche Einarbeitung! |
| **Installation und Integration** | ✔️ Einfache Integration, da SQLite bereits in Python enthalten ist und keine zusätzliche Installation benötigt wird. | ❌ Erfordert Installation und Einrichtung von Firebase SDKs sowie die Konfiguration eines Firebase-Projekts. |
| **Datensicherheit und -sicherung** | ❔ Sicherung und Wiederherstellung müssen manuell verwaltet werden. Sicherheit hängt von der Implementierung ab. | ✔️ Eingebaute Sicherheitsregeln, automatisierte Backups und Datenwiederherstellungsmöglichkeiten. | 

---
## 04: Verwendung von Mapbox

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 26.07.2024

### Problem statement

Um eine Karte von Europa auf der Homepage unserer Anwendung anzeigen zu lassen, benötigen wir eine Plattform, welche uns eine API zur Verfügung stellt, die wir in unser Projekt einbinden können.

Entscheidung getroffen von: Eliana Kaping, Rojin Aylin Aslan, Johanna Engels

### Decision

Unsere Entscheidung fiel auf Mapbox.
Mapbox bietet ein kostenfreies Nutzungslimit an und bietet uns durch seine hohe Anpassbarkeit und Flexibilität bei der Gestaltung von Kartenstilen und -features die Möglichkeit, die Visualisierung so zu gestalten, wie es uns gefällt.

### Regarded options

| Criterion | Mapbox | Google Maps |
| --- | --- | --- |
| **Know-how** | ❔ Es gibt eine steile Lernkurve bei der Anpassung und Nutzung, aber eine hohe Dokumentation | ✔️ Viele Entwickler sind bereits vertraut mit Maps und es gibt umfangreiche Dokumentation und Tutorials |
| **Aussehen anpassen** | ✔️ Hohe Anpassbarkeit: Kartendesigns können detailliert angepasst werden, einschließlich Farben und Stile etc. | ❌ Eingeschränkte Anpassungsfähigkeit im Vergleich zu Mapbox, bietet jedoch Werkzeuge für Anpassungen |
| **Verwendung** | ✔️ Muss über ein API-Schlüssel in das Projekt integriert werden, wobei viele SDKs und Bibliotheken verfügbar sind | ✔️ Weit verbreitet, einfache Integration über API-Schlüssel und umfangreiche Unterstützung in vielen Frameworks |
| **Kosten** | ✔️ Kann kostenlos genutzt werden (mit kostenlosem Kontingent), ideal für kleine bis mittelgroße Projekte | ❌ Kostenpflichtig nach einem begrenzten kostenlosen Kontingent, oft teurer für größere Projekte oder höhere Nutzung |  

---