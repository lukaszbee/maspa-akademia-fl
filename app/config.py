# definiujemy clase config

class Config(object):
    SECRET_KEY = 'tajnehaslo'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.bazamaspa'
    SQLALCHEMY_TRACK_MODIFICATION = False


maspa_logowanie = {'user': 'maspa', 'haslo': 'Monika00'}