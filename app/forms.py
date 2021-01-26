from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

# formularz logowania

class Logowanie(FlaskForm):
    user = StringField('User', validators=[DataRequired()])
    haslo = PasswordField('Haslo', validators=[DataRequired()])
    zatwierdz = SubmitField('Zatwierdz')
    pamietaj = BooleanField('Pamietaj')


# formularz dodawania kursow 

class Kursy_add(FlaskForm):
    nazwa = StringField('Nazwa kursu: ', validators=[DataRequired()])
    opis = TextAreaField('Opis kursu: ', validators=[DataRequired()])
    cena = StringField('Cena kursu: ', validators=[DataRequired()])
    dodaj = SubmitField('Dodaj')
