from flask import render_template, request, redirect, session
from flask.helpers import flash

from flask_app.models.user import User
from flask_app.models.priv_wall import Message

from flask_app import app

@app.route('/wall/<int:user_id>')
def wall_index(user_id):
    all_users = User.get_all_users()
    print(all_users)
    messages = Message.get_messages(user_id)
    return render_template('wall_index.html', all_users = all_users, all_messages = messages, current_id = user_id)

@app.route('/send_message', methods=['POST'])
def create_message():
    data = {
        'message': request.form['message'],
        'sender_id': request.form['sender_id'],
        'recipient_id': request.form['recipient']
    }
    Message.save(data)
    return redirect(f'/wall/{session["id"]}')

@app.route('/delete/<int:message_id>', methods=['POST'])
def delete_message(message_id):
    Message.delete(message_id)
    return redirect(f'/wall/{session["id"]}')