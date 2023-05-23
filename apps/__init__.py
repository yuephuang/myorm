from flask import Flask

from apps.app_email.route import bl_email
from apps.app_user.route import bl_user
from site_start import mail, db

from config.Config import create_config

configs = create_config()


def create_app():
    app = Flask(__name__)
    app.config.update(configs)

    mail.init_app(app)
    db.init_app(app)
    app.register_blueprint(bl_email)
    app.register_blueprint(bl_user)

    with app.app_context():
        db.create_all()
        print(1)
    return app



