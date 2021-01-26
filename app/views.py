from app import app, db
from flask import render_template, redirect, url_for
from app.forms import Logowanie, Kursy_add
from app.config import maspa_logowanie
# importujemy rzeczy do logowania 

from app.db_models import User, Kursy
from flask_login import current_user, login_user, login_required, logout_user


# znaczniki i dekoratory poszczegolnych stron 

@app.route('/')
def index():
    return render_template('index.html')

''' @app.route('/logowanie', methods=['GET', 'POST'])
def logowanie():
    form = Logowanie()
    if form.validate_on_submit():
        if form.user.data == maspa_logowanie.get('user') and form.haslo.data == maspa_logowanie.get('haslo'):
            return redirect(url_for('paneladmina'))
    return render_template('logowanie.html', form=form) '''

@app.route('/logowanie', methods=['GET', 'POST'])
def logowanie():
    if current_user.is_authenticated:
        return redirect(url_for('paneladmina'))
    form = Logowanie()
    if form.validate_on_submit():
        gosc = User.query.filter_by(user=form.user.data).first()
        # pobranie rekordu z bazy

        if gosc and gosc.haslo == form.haslo.data:
            login_user(gosc, remember=form.pamietaj.data)
            return redirect(url_for('paneladmina'))
            # jesli login i user sie zgadza przekirowuje do panelu admina

        elif gosc is None :
            return f'nie ma takiego usera'
            # jesli nie ma usera zwraca info

        else:
            return f'zle haslo'
            # jesli bledne haslo zwraca info
    return render_template('logowanie.html', form=form)

@app.route('/logowanie/paneladmina', methods=['GET', 'POST'])
@login_required
def paneladmina():
    kursy = Kursy.query.all()
    return render_template('panel.html', kursy=kursy)


@app.route('/kursedit', methods = ['GET', 'POST'])
@login_required
def kursedit():
    form = Kursy_add()
    if form.validate_on_submit():
        kurs = Kursy(nazwa= form.nazwa.data , opis= form.opis.data , cena= form.cena.data)
        db.session.add(kurs)
        db.session.commit()
        return redirect(url_for('paneladmina'))
    return render_template('kursedit.html', form=form)

# usuwanie kursow 
@app.route('/del/<int:id>', methods=['GET', 'POST'])
@login_required
def del_kurs(id: int):
    kurs_del= Kursy.query.filter_by(id=id).first()
    db.session.delete(kurs_del)
    db.session.commit()
    return redirect(url_for('paneladmina'))

# edycja kursow 

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_kurs(id: int):
    kurs_edit= Kursy.query.filter_by(id=id).first()
    form = Kursy_add()
    if form.validate_on_submit():
        kurs_edit.nazwa=form.nazwa.data 
        kurs_edit.opis= form.opis.data
        kurs_edit.cena= form.cena.data
        try:
            db.session.add(kurs_edit)
            db.session.commit()
            return redirect(url_for('paneladmina'))
        except:
            return f'Cos poszlo nie tak'
    return render_template('kursedit.html', form=form)

# strona z kursami 

@app.route('/kursypage')
def kursypage():
    kursy = Kursy.query.all()
    return render_template('kursy.html', kursy=kursy)

@app.route('/kursdetal/<int:id>')
def kursdetak(id: int):
    kurs = Kursy.query.filter_by(id=id).first()
    return render_template('kursdetal.html', kurs=kurs)

# strona kontakt 

@app.route('/kontakt')
def kontakt():
     return render_template('kontakt.html')


# strona trenerow 

@app.route('/trenerzy')
def trenerzy():
    return render_template('trenerzy.html')


# funkcja do wylogowania usera 

@app.route('/loguot')
def logout():
    logout_user()
    return render_template('index.html')