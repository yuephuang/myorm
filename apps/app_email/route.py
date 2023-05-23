import datetime

import jwt

from flask import Blueprint, request

from apps.app_email.control import send_message
from config.salt_config import MAIL_SALT

bl_email = Blueprint('email', __name__, url_prefix='/email')

salt = MAIL_SALT


# 重置密码
@bl_email.route('/reset', methods=['GET', 'POST'])
def reset_password():
    username = request.json.get('username'),
    user_email = request.json.get('email')
    email_title = f"你好，{username}, 重置密码"
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    payload = {
        "username": username,
        "exp": expiration_time
    }
    token = jwt.encode(payload, salt, algorithm='HS256')
    email_body = f"请点击链接进行密码重置, http://127.0.0.1:5000/email/{token}"
    send_message(email_title, email_body, recipients=[user_email])
    return str(email_body)


@bl_email.route('/<token>', methods=['GET'])
def check_token(token):
    decoded_payload = jwt.decode(token, salt, algorithms=['HS256'])

    return decoded_payload

