import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Wczytujemy plik .env (niewidoczny dla pobierających na Github)
load_dotenv()

# Bezpiecznie zaciągamy klucz API
API_KEY = os.environ.get("API_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/Pogoda'
db = SQLAlchemy(app)

class Historia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    miasto = db.Column(db.String(100), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        zlapane_miasto = request.form['city']

        url = f"http://api.openweathermap.org/data/2.5/weather?q={zlapane_miasto}&appid={API_KEY}&units=metric"

        odpowiedz = requests.get(url)
        dane_pogodowe = odpowiedz.json()

        if dane_pogodowe.get('cod') == 200:
            nowy_wpis = Historia(miasto=zlapane_miasto)
            db.session.add(nowy_wpis)
            db.session.commit()

        widoczna_historia = Historia.query.order_by(Historia.id.desc()).limit(3).all()

        return render_template('index.html', dane_pogodowe=dane_pogodowe, pelna_historia=widoczna_historia)

    widoczna_historia = Historia.query.order_by(Historia.id.desc()).limit(3).all()

    return render_template('index.html', pelna_historia=widoczna_historia)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)