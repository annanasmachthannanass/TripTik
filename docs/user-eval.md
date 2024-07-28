---
title: User Evaluation
nav_order: 4
---

{: .no_toc }
# User evaluation

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Reise hinzufügen

### Meta

Status
: Work in progress - **Done** - Obsolete

Updated
: 22-07-2024

### Goal

Ziel dieser User-Evaluation war es, herauszufinden, wie intuitiv und nutzerfreundlich die Anwendung ist. Dabei stand hier vor allem das Hinzufügen einer Reise bzw. die vollständige Dokumentation der Reise im Vordergrund, um herauszufinden, ob es spezifische Hürden oder Schwierigkeiten bei der Nutzung dieser Funktion gibt.

### Method

#### Teilnehmer

An der Evaluation nehmen 10 Nutzer, Freunde und Familie, teil, welche die Anwendung zum ersten Mal verwenden und keine Erfahrungen mit jeglichen Reisetracker-Apps, wie beispielsweise Polarsteps, haben.

#### Ablauf

> Dabei bekamen alle Nutzer die Aufgabe, sich zuerst zu registrieren und anschließend einzuloggen. Dazu werden sie aufgefordert, einen Nutzernamen und ein Passwort einzugeben, um nachdem den Registrieren-Button zu drücken. Nach der Nachricht, dass das Erstellen, eines Accounts erfolgreich war, kehren die Nutzer zum Login zurück und melden sich mit den erstellten Nutzerdaten an. Somit werden sie direkt zu dem Home-Screen weitergeleitet und können von dort aus in der Seitenleiste eine Reise hinzufügen.

> Anschließend waren die Nutzer in der Lage dazu, einen Titel für die Reise, das Land, die Stadt, das Start- und das Enddatum, einen Bericht und die entsprechenden Bilder in die dafür vorgesehenen Felder einzufügen. Schlussendlich musste nur noch der Hinzufügen Button am unteren Bildschirmrand betätigt werden und die Reise wurde erfolgreich hinzugefügt.

> Während die Nutzer diese Schritte durchlaufen haben, wurden sie dazu aufgefordert, die Zeit zu stoppen und sämtliche Erfahrungen sowie Schwierigkeiten mitzuteilen.

### Results

> Dabei ergab sich, dass die durchschnittliche Zeit zur Erledigung der Aufgabe, inklusive des Registrierens, des Einloggens und des Erstellens einer Reise, bei 5 bis 10 Minuten lag. Diese Spanne unterscheidet sich je nachdem, wie lang der erstellte Bericht der Nutzer war und wie viele Fotos hinzugefügt wurden.

> Zudem fanden 4 der 10 Nutzer das Hochladen der Bilder umständlich, da die Bilder nicht angezeigt wurden, sondern nur der Name der Datei präsentiert wurde.

### Implications

Durch diese Evaluation haben wir festgestellt, dass wir die Funktion zum Hochladen der Bilder verbessern müssen, um sie benutzerfreundlicher zu gestalten. Dafür haben wir sichergestellt, dass die ausgewählten Bilder angezeigt werden, statt dem Namen der Datei.

---

## 02: Mapbox Integration

### Meta

Status
: Work in progress - **Done** - Obsolete

Updated
: 25-07-2024

### Goal

Um die verschiedenen Länder, die bereits bereist wurden, zu visualisieren, haben wir Mapbox verwendet. Nun möchten wir herausfinden, wie zufrieden unsere Testnutzer mit der Kartenfunktion sind. Insbesondere wollen wir wissen, ob die Nutzer die farbliche Markierung der bereits bereisten Länder als informativ empfinden.

### Method

#### Teilnehmer

An der Evaluation nehmen erneut 10 Nutzer, Freunde und Familie, teil, welche die Anwendung bereits ein Mal verwendet haben, jedoch keine weiteren Erfahrungen mit anderen Reisetracker-Apps, wie beispielsweise Polarsteps, haben.

#### Ablauf

> Dabei bekamen alle Nutzer die Aufgabe, sich mit dem Account, der bei der letzten Evaluation erstellt wurde, einzuloggen. Nachdem dann der Nutzername und das Passwort eingegeben und der Login-Button betätigt wurden, werden die Nutzer direkt zu dem Home-Screen weitergeleitet und können von dort aus bereits die farbliche Markierung der Länder sehen, da sie schon bei der letzten Evaluation einige Reisen eingetragen haben.

> Die Nutzer waren diesmal in der Lage dazu, die verschiedenen Länder zu betrachten und mit der Karte zu interagieren, indem sie umherscrollen und prüfen, ob die richtigen Länder markiert wurden.

> Auch hier wurden die Nutzer dazu aufgefordert, während sie diese Schritte durchlaufen haben, sämtliche Erfahrungen sowie Schwierigkeiten mitzuteilen.

### Results

> Dabei ergab sich, dass 8 der 10 Nutzer die Markierungen als hilfreich empfanden.

> Ein Problem, das aufgetreten ist, war jedoch, dass einige Länder nicht markiert wurden. Das lag daran, dass die Länder in der Geojson-Datei auf Englisch eingetragen sind, einige Nutzer jedoch den deutschen Namen in die Reise eingetragen haben.

### Implications

Durch diese Evaluation ist uns aufgefallen, dass wir die Länder aus der Datei übersetzen müssen und einheitlich festlegen müssen, dass die Anwendung auf Deutsch ist, damit keine weitere Verwirrung für die Nutzer entsteht. 

---

## 03: Progress Bar

### Meta

Status
: Work in progress - **Done** - Obsolete

Updated
: 28-07-2024

### Goal

Die User-Evaluation sollte herausfinden, wie verständlich und motivierend die Nutzer die Progress Bar, die den Prozentsatz der bereisten Länder anzeigt, empfinden. Dabei legen wir den Fokus auf die Verständlichkeit und Klarheit der Progress Bar.

### Method

#### Teilnehmer

An der Evaluation nehmen auch hier die 10 Nutzer, Freunde und Familie, teil, welche die Anwendung während der ersten zwei Evaluationen verwendet haben, jedoch keine weiteren Erfahrungen mit anderen Reisetracker-Apps, wie beispielsweise Polarsteps, haben.

#### Ablauf

> Dabei bekamen die Nutzer erneut die Aufgabe, sich mit dem Account, welcher bereits erstellt wurde, einzuloggen. Nachdem dann der Nutzername und das Passwort eingegeben und der Login-Button betätigt wurden, werden die Nutzer direkt zu dem Home-Screen weitergeleitet und können von dort aus neben der farblichen Markierung der Länder nun auch die Progress Bar sehen.

> Die Nutzer waren nun in der Lage dazu, neben den verschiedenen Ländern, die farblich markiert waren, den Fortschritt visuell dargestellt und den entsprechenden Prozentsatz angezeigt zu bekommen.

> Erneut wurden die Nutzer dazu aufgefordert, während sie diese Schritte durchlaufen haben, sämtliche Erfahrungen sowie Schwierigkeiten mitzuteilen.

### Results

> Dabei ergab sich, dass alle der 10 Nutzer den dargestellten Progress und den Prozentsatz als hilfreich und verständlich empfanden. 

> Jedoch teilten 2 der 10 Nutzer mit, dass der Prozentsatz schwer zu erkennen ist aufgrund der Farbe des Textes.

### Implications

Durch diese Evaluation haben wir festgestellt, dass die Nutzer dieses Feature sehr wertschätzen, dass wir jedoch an der Darstellung nochmal arbeiten müssen. Aus diesem Grund haben wir uns dazu entschieden, eine Leiste hinter die Progress Bar und den Prozentsatz einzufügen, die zu 50% transparent ist. So haben die Nutzer die Möglichkeit, den Prozentsatz sowohl auf einem hellen als auch auf einem dunkelen Hintergrund gut lesbar zu betrachten.

---
