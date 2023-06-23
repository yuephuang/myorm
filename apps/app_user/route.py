from flask import Blueprint, request

from apps.app_email.control import send_message

bl_user = Blueprint("user", __name__, url_prefix="/user")


@bl_user.route('/register', methods=['GET', 'POST'])
def register():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    reset_password = request.json.get('reset_password')
    if password != reset_password:
        return f"账号密码不一致"
    if not all([username, email, password, reset_password]):
        return "请正确输入账号密码邮箱"
    send_message("注册邮件", "这是注册测试", recipients=[email])

    return "注册链接已发送到你的邮箱，请注意查收"


@bl_user.route('/login')
def login():
    # 前后端分离这个需要jwt
    pass
