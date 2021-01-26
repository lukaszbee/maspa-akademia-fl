# import podstawowych modulow

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# import pliku config 
from app.config import Config

# zdefiniowanie  apki !!!
# -----------------

app = Flask(__name__)
app.config.from_object(Config)


# zdefinowanie bazy danych !!! 

db = SQLAlchemy(app)

# zainicjowanie login managera !!!

login = LoginManager(app)

# zaimpoprtowanie plikow widoku i baz danych !!!

from app import views, db_models