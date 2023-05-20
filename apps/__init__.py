from flask import Flask

from apps.app_email.route import bl_email
from site_start import mail

from config.Config import create_config

configs = create_config()


def create_app():
    app = Flask(__name__)
    app.config.update(configs)

    mail.init_app(app)
    app.register_blueprint(bl_email)
    return app



