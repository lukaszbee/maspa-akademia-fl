inicjowanie bazy danych w SQLalchemy:

odpala konsole pythona -> polecenie python3
>>> from app import db
>>> db.create_all()
>>> from app.db_models import User
>>> u1 = User(user='paula', haslo='Monika00')
>>> db.session.add(u1)
>>> db.session.commit()
>>> u2 = User(user='gosia', haslo='Monika00')
>>> db.session.add(u2)
>>> db.session.commit()

wejscie do bazy -> polecenie
sqlite3 app/db.bazamaspa 
sqlite> SELECT * FROM user;
1|paula|Monika00
2|gosia|Monika00

logowanie : 
dziala bez modulu :
    # if current_user.is_authenticated:
    #     return redirect(url_for('index'))
<!-- nie wiem czemu  -->