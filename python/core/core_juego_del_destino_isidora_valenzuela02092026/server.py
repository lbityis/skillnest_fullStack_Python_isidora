import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "key"

# Muestras de predicciones reducidas
PREDS = [
    {"ok": True, "ico": "bi-star-fill", "txt": "Encontrarás el verdadero amor pronto."},
    {"ok": True, "ico": "bi-gem", "txt": "Una oportunidad financiera aparecerá."},
    {"ok": False, "ico": "bi-exclamation-triangle-fill", "txt": "Ten cuidado con decisiones impulsivas."},
    {"ok": False, "ico": "bi-cloud-rain-fill", "txt": "Un pequeño obstáculo te dejará enseñanza."}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    # Guardar datos resumidos en la sesión
    session['nom'] = request.form.get('nom')
    session['eda'] = request.form.get('eda')
    session['col'] = request.form.get('col')
    session['ani'] = request.form.get('ani')
    session['prd'] = random.choice(PREDS)
    session['num'] = random.randint(1, 99)
    return redirect(url_for('out'))

@app.route('/futuro')
def out():
    if 'nom' not in session:
        return redirect(url_for('home'))
    return render_template('futuro.html')

if __name__ == '__main__':
    app.run(debug=True)