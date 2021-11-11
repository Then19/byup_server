from flask import render_template, request, jsonify
from app import app
from SQLcon import *


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello, world!'


@app.route('/get_messages')
def get_all_messages():
    data = get_messages()
    return {'data': data}


@app.route('/add_message', methods=['POST'])
def add_msg():
    name = request.form.get('username')
    msg = request.form.get('message')
    if name and msg:
        add_message(name, msg)
        return {'status': True}
    return {'status': False, 'warn': 'какая то ошибка'}
