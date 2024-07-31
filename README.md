TripTik 
- Gruppenarbeit in Entwicklung von Webanwendungen im Somersemester 2024

Link zur Dokumentation: https://annanasmachthannanass.github.io/TripTik/

Gruppenmitglieder:
Eliana Kaping (el231204),
Rojin Aylin Aslan (rrayas22),
Johanna Engels (annanasmachthannanass)

Schritte zum Ausführen der Applikation:

Voraussetzungen
Python (Version 3.6 oder höher)
Git

Schritt-für-Schritt Anleitung
- Klonen Sie das GitHub-Repository auf Ihren lokalen Rechner.
- Erstellen Sie eine virtuelle Umgebung, um Abhängigkeiten isoliert zu installieren. Führen Sie dazu den folgenden Befehl aus:
python -m venv venv
- Installieren Sie die benötigten Abhängigkeiten, die in der requirements.txt Datei aufgeführt sind:
pip install -r requirements.txt

Erstellen der Datenbank
- Sie wurde nicht in des Repository integregiert, da es dadurch immer zu Problemen kam.
- Setzen sie die Variable FLASK_APP, um das richtige Programm zu starten:
set FLASK_APP=create_tables.py
flask run
- Schreiben Sie nun nacheinander in die URL des Browsers, um die notwendigen Tabellen zu erstellen
http://127.0.0.1:5000/create_users_table
http://127.0.0.1:5000/create_trips_table
http://127.0.0.1:5000/add_profile_picture_column
http://127.0.0.1:5000/add_bio_column
http://127.0.0.1:5000/add_images_table

Nun können Sie TripTik ausführen.
- Beenden sie dafür zunächst die aktuelle Anwendung mit CTRL+C
- Setzen sie nun home.py als FLASK_APP
set FLASK_APP=home.py
- Öffnen sie nun im Browser http://127.0.0.1:5000/ um TripTik zu starten. Sie sollten nun auf der Startseite sein und sich registrieren können.

Problemlösung
Falls Sie auf Probleme stoßen, überprüfen Sie die folgenden Punkte:
Stellen Sie sicher, dass alle Abhängigkeiten korrekt installiert sind.
Stellen Sie sicher, dass die virtuelle Umgebung aktiviert ist.
