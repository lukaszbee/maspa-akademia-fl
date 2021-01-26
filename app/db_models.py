from app import db , login
from flask_login import UserMixin


# inicjuje baze danych do przechowywanie urzytkownikow i hasel 

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), nullable=False)
    haslo = db.Column(db.String(15), nullable=False)

# baza danych dla kyrsow

class Kursy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(150), nullable=False)
    opis = db.Column(db.Text, nullable=False)
    cena = db.Column(db.String(25), nullable=False)

# inicjuje funkcje user loader z LoginManagera 

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

