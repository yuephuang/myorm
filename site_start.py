from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO

mail = Mail()
db = SQLAlchemy()
login = LoginManager()
socketio = SocketIO()
