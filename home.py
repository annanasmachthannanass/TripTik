from flask import Flask, render_template, request

# flask run --reload zum starten des Servers
# mit --reload wird der Server bei Änderungen neu gestartet
# Ausnahme: bei DB oder Template Änderungen

# falls es nicht funktioniert, kann es sein, dass die Umgebungsvariable FLASK_APP nicht gesetzt ist
# dafür einfach FLASK_APP=TirpTik/home.py setzen

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

@app.route('/profil_bearbeiten', methods=['POST'])
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


if __name__ == '__main__':
    app.run(debug=True)