from datetime import datetime

from site_start import db
from sqlalchemy import CheckConstraint
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    address = db.Column(db.String(200))
    create_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    update_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(2))
    avatar_url = db.Column(db.String(255))
    __table_args__ = (
        CheckConstraint("gender IN ('male', 'female')", name='valid_gender'),
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Encourage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    author = db.Column(db.String(255))
    message = db.Column(db.String(255))
    create_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    update_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    score = db.Column(db.String(255))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer)
    receive_id = db.Column(db.Integer)
    sender_type = db.Column(db.Integer)
    receive_type = db.Column(db.Integer)
    msg_type = db.Column(db.Integer)
    msg_status = db.Column(db.Integer)
    content = db.Column(db.String(255))
    timestamp = db.Column(db.Integer)
    sender_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    receive_datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)
