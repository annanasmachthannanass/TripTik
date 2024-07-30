---
title: Architecture
parent: Technical Docs
nav_order: 1
---

{: .no_toc }
# Architecture

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Overview

TripTik ist ein umfassendes Reise-Tool, das entwickelt wurde, um Nutzern dabei zu helfen, ihre Reiseerfahrungen auf unterhaltsame und interaktive Weise zu dokumentieren und zu verwalten.

### Kernfunktionalität

Die Kernfunktionalität unserer Anwendung dreht sich um ein detailliertes Reisetagebuch-System, in das Benutzer Informationen über ihre Reisen, einschließlich Reiseziele, Daten und persönliche Notizen, eingeben können. 

> Diese Daten fließen in mehrere zentrale Funktionen ein:

1. **Interaktive Kartenintegration:**
+ TripTik verwendet Mapbox, um eine interaktive Weltkarte anzuzeigen, auf der die Nutzer die Länder markieren können, die sie besucht haben. Diese Karte bietet eine visuelle Darstellung der Reise und des Reiseverlaufs.

2. **Verfolgung des Reiseverlaufs:**
+ Eine Progress Bar berechnet und zeigt an, wie viel Prozent der Welt der Nutzer bereits bereist hat und motiviert so zu weiteren Abenteuern. Diese Funktion basiert auf der Anzahl der besuchten Länder im Verhältnis zur Gesamtzahl der in der Anwendung verfügbaren Länder.

3. **Verwaltung und Anzeige von Inhalten:**
+ Die Nutzer können umfangreiche Reiseberichte erstellen, die Texte, Bilder und andere Inhalte enthalten. Diese Einträge sind mit Ländern auf der Karte verknüpft und bieten einen umfassenden Überblick über jede Reise.

### Systemarchitektur

> Die Architektur unserer Anwendung basiert auf einem Client-Server-Modell, das für die Gewährleistung der Datenintegrität und für robuste Benutzerinteraktionen unerlässlich ist. Diese Struktur unterstützt eine sichere Datenverarbeitung und bietet eine konsistente Benutzererfahrung über verschiedene Geräte hinweg.

> Durch die klare Trennung zwischen Client und Server erhöht man nicht nur die Sicherheit, sondern verbessert auch die Wartbarkeit und Skalierbarkeit der Anwendung. Neue Funktionen können so auf der Client-Seite hinzugefügt werden, ohne dass tiefgreifende Änderungen auf der Server-Seite vorgenommen werden müssen und umgekehrt.

#### Client-Seite: 

> Die Client-Seite besteht aus einer Webanwendung, die im Browser des Benutzers läuft. Diese Webanwendung dient als Schnittstelle und verarbeitet alle Benutzerinteraktionen, einschließlich der Eingabe von Reisedaten und der Anzeige von Informationen.

+ **Technologien:** HTML, [CSS](https://annanasmachthannanass.github.io/TripTik/design-decisions.html#01-frontend-design-method), [JavaScript](https://annanasmachthannanass.github.io/TripTik/design-decisions.html#02-verwendung-von-javascript) und [Mapbox](https://annanasmachthannanass.github.io/TripTik/design-decisions.html#04-verwendung-von-mapbox) für die interaktive Kartenintegration.
+ **Datenkommunikation:** Die Client-Seite kommuniziert mit dem Server über HTTP-Anfragen, wobei die Datenformate JSON bzw. GeoJSON verwendet werden, um Informationen wie Kartenkoordinaten und Reisedaten zu übertragen. Diese Datenformate sind ideal für die Übertragung komplexer geografischer Informationen und strukturierter Daten.
+ **Echtzeitsynchronisation:** Die Synchronisation zwischen Client und Server erfolgt in Echtzeit, um sicherzustellen, dass alle Benutzeraktionen sofort reflektiert werden, sei es das Hinzufügen neuer Reisedaten oder das Aktualisieren des Fortschrittsbalkens.

#### Server-Seite: 

> Die Server-Seite wird von einem Python-basierten Back-End verwaltet, das auf dem Flask-Framework aufbaut. Flask bietet eine flexible und leichtgewichtige Basis für die Entwicklung von Webanwendungen.

+ **Datenverarbeitung:** Der Server ist für die Verarbeitung der Benutzereingaben zuständig. Er validiert die Daten, wendet die Geschäftslogik an und aktualisiert die Datenbank entsprechend.
+ **Datenbank:** Als Datenbanksystem verwenden wir [SQLite](https://annanasmachthannanass.github.io/TripTik/design-decisions.html#03-datenbankl%C3%B6sung), da sich diese leichtgewichtige, relationale Datenbank ideal für die Anforderungen unserer Anwendung eignet, insbesondere für die Speicherung und Verwaltung von Reisedaten und Benutzerinformationen.
+ **Templating und Rendering:** Mit Jinja generiert der Server dynamische HTML-Seiten, die dann an den Client gesendet werden. Dies ermöglicht uns eine nahtlose Integration der Backend-Logik mit der Präsentationsschicht und stellt sicher, dass die Benutzer stets aktuelle und relevante Informationen sehen.
---

## Codemap

### Projektstruktur

> Unsere Anwendung ist in mehrere Module unterteilt, die jeweils spezifische Funktionalitäten abdecken. Zu den wichtigsten Bestandteilen gehören:

#### home.py

+ `home.py` ist verantwortlich für die Verwaltung der Routen und der Logik, die die Hauptseiten der Anwendung bedienen. Sie stellt sicher, dass die Benutzer die richtigen Inhalte sehen und dass die Anfragen korrekt verarbeitet werden.

**Flask-Anwendung und Konfiguration**
+ Die Flask-Anwendung wird im ersten Schritt mit app = Flask(__name__) initialisiert. Zudem wird eine secret_key wird gesetzt, der für die Sitzungsverwaltung und den CSRF-Schutz verwendet wird.
+ Zudem definiert die Datei Pfade für die Datenbank und andere Ressourcen, wie beispielsweise GeoJSON- und JSON-Dateien, die innerhalb der Anwendung verwendet werden.

**Datenbankverwaltung**
+ Die get_db() Funktion wird definiert, um eine Verbindung zur SQLite-Datenbank herzustellen. Zudem prüft check_db_connection() die die Datenbankverbindung.

**Benutzerverwaltung**
+ Weiterhin gibt es Endpunkte (/register und /login), die Benutzereingaben entgegennehmen und in der Datenbank speichern. Hier werden auch das Passwort-Hashing und Sitzungsmanagement implementiert.
+ Die Datei verwendet außerdem generate_password_hash und check_password_hash, um Benutzerdaten zu schützen.

**Reiseverwaltung**
+ Funktionen wie reise_speichern und reise_aendern verwalten das Speichern und Aktualisieren von Reiseinformationen in der Datenbank. Diese Funktionen verarbeiten zudem Bilder, die von Benutzern hochgeladen wurden.
+ Auch gibt es Funktionen zum Abrufen von Reiseinformationen, wie get_trip, get_trip_images, get_trip_list, und get_trip_country_list, die Informationen aus der Datenbank abrufen und für die Anzeige in der App vorbereiten.

**Routen**
+ Weiterhin sind die Routen in der Flask-Anwendung enthalten. Diese definieren, wie verschiedene HTTP-Anfragen behandelt werden und welche Vorlagen bzw. Templates gerendert werden. Hier ist eine Beschreibung der einzelnen [Routen](https://annanasmachthannanass.github.io/TripTik/technical-docs/reference.html).

#### templates

+ Der Ordner `templates` enthält sämtliche HTML-Templates, die in der Anwendung verwendet werden. Diese Templates werden mit Jinja, einem Template-Engine für Python, gerendert. Jinja ermöglicht uns, dynamische Inhalte in HTML-Dateien einzufügen, indem es Platzhalter und Kontrollstrukturen wie Schleifen und Bedingungen verwendet.

+ Jedes Template repräsentiert dabei eine spezifische Seite oder einen Teil der Benutzeroberfläche von TripTik. Beispielsweise kann bei unserer Anwendung zwischen Templates für die Startseite, die Detailansicht einer Reise, das Bearbeiten einer Reise und das Hinzufügen einer neuen Reise unterschieden werden.

+ Die Templates sind dabei so strukturiert, dass sie wiederverwendbare Komponenten enthalten, wie z.B. Kopf- und Fußzeilen, die in mehreren Seiten verwendet werden können. Dies fördert die Konsistenz im Design und erleichtert die Wartung der Anwendung.

#### static

+ Der `static`-Ordner enthält alle statischen Dateien der Anwendung. Diese Dateien werden direkt vom Webserver an den Client ausgeliefert und ändern sich nicht dynamisch. Zu den statischen Dateien gehören:

**CSS-Dateien**
+ Diese Dateien enthalten die Stylesheets, die das Aussehen und Layout der HTML-Seiten definieren. Sie sorgen für ein konsistentes Design und ermöglichen es, das Erscheinungsbild der Anwendung zentral zu verwalten.

**JavaScript-Dateien** 
+ Die JavaScript-Dateien enthalten clientseitige Skripte, die die Interaktivität und Funktionalität der Anwendung verbessern. Sie können für Formvalidierung, AJAX-Anfragen, Animationen und vieles mehr verwendet werden.
    
**Images**
+ Alle Bilder, die in der Anwendung verwendet werden, werden im `static`-Ordner gespeichert. Dies können Logos, Hintergrundbilder, Icons und andere grafische Elemente sein.

**JSON-Dateien**
+ Der `geojson`-Ordner enthält GeoJSON-Dateien, die geografische Daten in einem JSON-basierten Format speichern. GeoJSON ist ein offenes Standardformat, das für die Darstellung von geografischen Merkmalen und deren Eigenschaften verwendet wird. Es wird häufig in Webanwendungen verwendet, um Karten und geografische Informationen darzustellen.
+ Eine typische GeoJSON-Datei enthält eine Sammlung von geografischen Merkmalen, die als `FeatureCollection` bezeichnet wird. In unserem Fall enthält die Datei Koordinaten für die Grenzen der einzelnen Länder, um die bereisten Länder der Nutzer farbig darzustellen.
---

## Cross-cutting concerns

### Sicherheit

> TripTik implementiert mehrere Sicherheitsmaßnahmen, um nicht nur die Integrität, sondern auch Vertraulichkeit der Benutzerdaten zu gewährleisten. Dazu gehören:

+ **Passwort-Hashing**: Die Passwörter der Nutzer werden mit einer sicheren Hashing-Funktion (`generate_password_hash`) gespeichert, um sicherzustellen, dass die jeweiligen Passwörter nicht im Klartext in der Datenbank gespeichert werden.
+ **Sitzungsmanagement**: Zudem werden die verschiedenen Benutzer nach der erfolgreichen Anmeldung in einer Sitzung (`session`) gespeichert, um den Zugriff auf geschützte Bereiche der Anwendung zu ermöglichen.
+ **Eingabevalidierung**: Alle Benutzereingaben werden sorgfältig validiert und behandelt, um SQL-Injection und andere Angriffe zu verhindern.

### Fehlerbehandlung und Logging

> Um eine robuste Fehlerbehandlung zu gewährleisten, haben wir ein zentrales Fehlerbehandlungssystem implementiert:

+ **Fehlerbehandlung**: Aufkommende Datenbankfehler werden abgefangen, wobei dann die entsprechenden Fehlermeldungen dem Benutzer angezeigt werden (`flash`), um eine bessere Benutzererfahrung zu gewährleisten.
+ **Logging**: Zudem werden die Fehler protokolliert, um eine einfache Diagnose und Behebung von Problemen zu ermöglichen.

### Wartbarkeit und Erweiterbarkeit

> Die Anwendung ist modular aufgebaut, um Wartung und Erweiterungen zu erleichtern:

+ **Modularität**: Jeder Funktionalitätsbereich, wie beispielsweise die Registrierung, Anmeldung oder Reiseverwaltung, ist in separaten Funktionen und Routen gekapselt, um die Wartbarkeit zu verbessern.
+ **Datenbankabstraktion**: Zudem sind alle Datenbankzugriffe in separaten Funktionen gekapselt (`get_trip`, `get_trip_images`, `get_trip_list`), um die Wiederverwendbarkeit und Testbarkeit zu erhöhen.

### [Routen](https://annanasmachthannanass.github.io/TripTik/technical-docs/reference.html) und Templates

> Mithilfe von Flask-Routen haben wir die Möglichkeit verschiedene Seiten und Funktionen bereitzustellen. Einige der genutzten Routen sind dabei folgende:

+ **Startseite** (`/`): Zeigt die Anmeldeseite an.
+ **Home-Seite** (`/home`): Zeigt die Startseite mit einer Liste von Ländern und dem Fortschritt des Benutzers an.
+ **Reisedetails** (`/reise`): Zeigt die Details einer spezifischen Reise an, basierend auf der Trip-ID.
+ **Reise hinzufügen** (`/reise_hinzufuegen`): Zeigt die Seite zum Hinzufügen einer neuen Reise an.
+ **Profilseite** (`/profil`): Zeigt die Profilseite des Benutzers an.