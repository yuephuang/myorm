from flask import Flask

from apps.app_chat.route import bl_chat
from apps.app_email.route import bl_email
from apps.app_user.route import bl_user
from apps.app_index.route import bl_index
from config.salt_config import SECRET_KEY
from site_start import mail, db, socketio

from config.Config import create_config

configs = create_config()


def create_app():
    app = Flask(__name__)
    app.config.update(configs)
    app.secret_key = SECRET_KEY

    mail.init_app(app)
    db.init_app(app)
    socketio.init_app(app)
    app.register_blueprint(bl_email)
    app.register_blueprint(bl_user)
    app.register_blueprint(bl_index)
    app.register_blueprint(bl_chat)
    #
    # with app.app_context():
    #     db.create_all()
    return app



