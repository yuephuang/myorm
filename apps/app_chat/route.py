from flask import Blueprint, request, session, redirect, url_for, render_template, jsonify
from flask_socketio import join_room, leave_room

from site_start import socketio
from dao.mysql_operation import ChatOperation

bl_chat = Blueprint('chat', __name__, url_prefix='/chat')

online_user = []
room_user = {}


@bl_chat.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if 'username' in session:
            return redirect(url_for('chat.chat'))
        return render_template('index.html')
    else:
        username = request.form.get('username')
        room = request.form.get('room')
        session['username'] = username
        session['room'] = room
        return redirect(url_for('chat.chat'))


@bl_chat.route('/chat/')
def chat():
    if 'username' in session and 'room' in session:
        username = session['username']
        room = session['room']
        return render_template('chat.html', username=username, room=room)
    else:
        return redirect(url_for('chat.index'))


@bl_chat.route('/logout/')
def logout():
    if 'username' in session:
        session.clear()
    return redirect(url_for('chat.index'))


# # 连接
@socketio.on('connect')
def handle_connect():
    username = session.get('username')
    online_user.append(username)


# 断开连接e
@socketio.on('disconnect')
def handle_disconnect():
    username = session.get('username')
    print('connect info:  ' + f'{username}  disconnect')


@socketio.on('send msg')
def handle_message(data):
    print('sendMsg' + str(data))
    room = session.get('room')
    data['message'] = data.get('message').replace('<', '&lt;').replace('>', '&gt;').replace(' ', '&nbsp;')
    socketio.emit('send msg',data, to=room)


@socketio.on('join')
def on_join(data):
    username = data.get('username')
    room = data.get('room')
    try:
        room_user[room].append(username)
    except:
        room_user[room] = []
        room_user[room].append(username)

    join_room(room)
    print('join room:  ' + str(data))
    print(room_user)
    socketio.emit('connect info', username + '加入房间', to=room)


@socketio.on('leave')
def on_leave(data):
    username = data.get('username')
    room = data.get('room')
    room_user[room].remove(username)
    leave_room(room)
    print('leave room   ' + str(data))
    print(room_user)
    socketio.emit('connect info', username + '离开房间', to=room)


@bl_chat.route('/send_msg', methods=['POST'])
def send_msg():
    msg = request.get_json()
    receive_id = msg.get('receive_id')
    sender_id = msg.get('sender_id')
    content = msg.get('content')
    if not all([sender_id, receive_id]):
        raise f'输入参数有误'
    ChatOperation().send_msg(sender_id=sender_id, receive_id=receive_id, content=content)
    return jsonify({"message": 'ok'})