from domain.table import User
from site_start import db


class UserOperation(object):

    @staticmethod
    def login(username, password, email):
        user = User(username=username, email=email)
        user.password = user.set_password(password)
        db.session.add(user)
        db.session.commit()
