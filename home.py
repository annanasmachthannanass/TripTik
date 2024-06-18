from flask import Flask, render_template, request


# flask run --reload zum starten des Servers
# mit --reload wird der Server bei Änderungen neu gestartet
# Ausnahme: bei DB oder Template Änderungen

# falls es nicht funktioniert, kann es sein, dass die Umgebungsvariable FLASK_APP nicht gesetzt ist
# dafür einfach set FLASK_APP=TirpTik/home.py setzen

app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def index():
    return render_template('home.html')
def home_clicked():
    return render_template('home.html')

@app.route('/profil', methods=['POST'])
def profil_clicked():
    # Hier können Sie die Logik einfügen, die ausgeführt werden soll, wenn der Button geklickt wird
    return render_template('profil.html')

@app.route('/profil_bearbeiten', methods=['GET', 'POST'])
def profil_bearbeiten_clicked():
    return render_template('profil_bearbeiten.html')

@app.route('/reisen', methods=['POST'])
def reisen_clicked():
    return render_template('reisen.html')

@app.route('/reise_bearbeiten', methods=['POST'])
def reise_bearbeiten_clicked():
    return render_template('reise_bearbeiten.html')

@app.route('/reise_hinzufügen', methods=['POST'])
def reise_hinzufügen_clicked():
    return render_template('reise_hinzufügen.html')

@app.route('/bucketlist', methods=['GET', 'POST'])
def bucketlist_clicked():
    return render_template('bucketlist.html')

@app.route('/quizzes', methods=['GET','POST'])
def quizzes_clicked():
    return render_template('quizzes.html')

# Albanien Quiz-Seite
@app.route('/albanien', methods=['GET', 'POST'])
def albanien():
    
   ## if request.method == 'GET':
    q1_answer = request.form.get('q1')
    q2_answer = request.form.get('q2')
    q3_answer = request.form.get('q3')

    score = 0
    if q1_answer == 'a':
        score += 1
    if q2_answer == 'c':
        score += 1
    if q3_answer == 'a':
        score += 1

    return render_template('albanien.html')
    ##return render_template('quiz_results.html', score=score)

@app.route('/quizresults', methods=['POST'])
def quiz_result():
    return render_template('quiz_results.html')

@app.route('/deutschland', methods=['POST'])
def deutschland():
    return render_template('deutschland.html')

@app.route('/finnland', methods=['POST'])
def finnland():
    return render_template('finnland.html')

@app.route('/frankreich', methods=['POST'])
def frankreich():
    return render_template('frankreich.html')

@app.route('/grossbritannien', methods=['POST'])
def grossbritannien():
    return render_template('grossbritannien.html')

@app.route('/italien', methods=['POST'])
def italien():
    return render_template('italien.html')

@app.route('/norwegen', methods=['POST'])
def norwegen():
    return render_template('norwegen.html')

@app.route('/oesterreich', methods=['POST'])
def oesterreich():
    return render_template('oesterreich.html')

@app.route('/polen', methods=['POST'])
def polen():
    return render_template('polen.html')

@app.route('/portugal', methods=['POST'])
def portugal():
    return render_template('portugal.html')

@app.route('/spanien', methods=['POST'])
def spanien():
    return render_template('spanien.html')

@app.route('/schweiz', methods=['POST'])
def schweiz():
    return render_template('schweiz.html')

@app.route('/schweden', methods=['POST'])
def schweden():
    return render_template('schweden.html')


@app.route('/stickerbuch', methods=['GET', 'POST'])
def stickerbuch():
    return render_template('stickerbuch.html')


# Error-Handler für 404-Fehler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.config['DEBUG'] = True  # Debug-Modus aktivieren
    app.run()  # Flask-Anwendung starten



    