import random

from domain.table import User, Encourage, Chat
from site_start import db

from utils.tools import time_to_timestamp

class UserOperation(object):

    @staticmethod
    def login(username, password, email):
        user = User(username=username, email=email)
        user.password = user.set_password(password)
        db.session.add(user)
        db.session.commit()


class IndexOperation(object):

    @staticmethod
    def encourage():
        encourage = Encourage()
        total = encourage.query.count()
        ids = random.randint(1, total)
        result = encourage.query.filter_by(id=ids).first()
        return {"text": result.text, "author": result.author}


class ChatOperation(object):

    @staticmethod
    def send_msg(sender_id, receive_id, content, msg_type='text'):
        chat = Chat(sender_id=sender_id, receive_id=receive_id, content=content, msg_type=msg_type, )
        chat.sender_type = 0
        chat.receive_type = 0
        chat.timestamp = time_to_timestamp()
        db.session.add(chat)
        db.session.commit()
        db.session
