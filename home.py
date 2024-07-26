from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os


# flask run --reload zum starten des Servers
# mit --reload wird der Server bei Änderungen neu gestartet
# Ausnahme: bei DB oder Template Änderungen

# falls es nicht funktioniert, kann es sein, dass die Umgebungsvariable FLASK_APP nicht gesetzt ist
# dafür einfach set FLASK_APP=TirpTik/home.py setzen

# falls es bei rojin nicht funktioniert -> export FLASK_APP=home.py <- in dem Terminal eingeben
# zum aktualisieren -> git checkout main <- und danach -> git pull origin main <-
# flask run --reload

app = Flask(__name__)

DATABASE = 'triptik_database.db'


#Routen für die verschiedenen Seiten
@app.route('/', methods=['GET','POST'])
def index():
    return render_template('anmeldungs.html')

@app.route('/home', methods=['GET','POST'])
def home():
    progress = 60
    return render_template('home.html', progress=progress)

@app.route('/reisen', methods=['GET', 'POST'])
def reisen_page():
    progress = 75
    return render_template('reisen.html', progress=progress)

@app.route('/profil', methods=['POST'])
def profil_page():
    return render_template('profil.html')

@app.route('/profil_bearbeiten', methods=['GET', 'POST'])
def profil_bearbeiten_page():
    return render_template('profil_bearbeiten.html')

@app.route('/profilbilder', methods=['GET'])
def profilbilder_page():
    return render_template('profilbilder.html')

@app.route('/reise_bearbeiten', methods=['POST'])
def reise_bearbeiten_page():
    return render_template('reise_bearbeiten.html')

@app.route('/reise_hinzufuegen', methods=['GET', 'POST'])
def reise_hinzufuegen_page():
    return render_template('reise_hinzufuegen.html')

# @app.route('/bucketlist', methods=['GET', 'POST'])
# def bucketlist_clicked():
#     return render_template('bucketlist.html')

# @app.route('/quizzes', methods=['GET','POST'])
# def quizzes_clicked():
#     return render_template('quizzes.html')

# # Albanien Quiz-Seite
# @app.route('/albanien', methods=['GET', 'POST'])
# def albanien():
    
#    ## if request.method == 'GET':
#     q1_answer = request.form.get('q1')
#     q2_answer = request.form.get('q2')
#     q3_answer = request.form.get('q3')

#     score = 0
#     if q1_answer == 'a':
#         score += 1
#     if q2_answer == 'c':
#         score += 1
#     if q3_answer == 'a':
#         score += 1

#     return render_template('quiz_seiten/albanien.html')
#     ##return render_template('quiz_results.html', score=score)

# @app.route('/quizresults', methods=['POST'])
# def quiz_result():
#     return render_template('quiz_results.html')

# @app.route('/deutschland', methods=['POST'])
# def deutschland():
#     return render_template('quiz_seiten/deutschland.html')

# @app.route('/finnland', methods=['POST'])
# def finnland():
#     return render_template('quiz_seiten/finnland.html')

# @app.route('/frankreich', methods=['POST'])
# def frankreich():
#     return render_template('quiz_seiten/frankreich.html')

# @app.route('/grossbritannien', methods=['POST'])
# def grossbritannien():
#     return render_template('quiz_seiten/grossbritannien.html')

# @app.route('/italien', methods=['POST'])
# def italien():
#     return render_template('quiz_seiten/italien.html')

# @app.route('/norwegen', methods=['POST'])
# def norwegen():
#     return render_template('quiz_seiten/norwegen.html')

# @app.route('/oesterreich', methods=['POST'])
# def oesterreich():
#     return render_template('quiz_seiten/oesterreich.html')

# @app.route('/polen', methods=['POST'])
# def polen():
#     return render_template('quiz_seiten/polen.html')

# @app.route('/portugal', methods=['POST'])
# def portugal():
#     return render_template('quiz_seiten/portugal.html')

# @app.route('/spanien', methods=['POST'])
# def spanien():
#     return render_template('quiz_seiten/spanien.html')

# @app.route('/schweiz', methods=['POST'])
# def schweiz():
#     return render_template('quiz_seiten/schweiz.html')

# @app.route('/schweden', methods=['POST'])
# def schweden():
#     return render_template('quiz_seiten/schweden.html')


# @app.route('/stickerbuch', methods=['GET', 'POST'])
# def stickerbuch():
#     return render_template('stickerbuch.html')


# Error-Handler für 404-Fehler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.config['DEBUG'] = True  # Debug-Modus aktivieren
    app.run()  # Flask-Anwendung starten

