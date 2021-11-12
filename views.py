from flask import render_template, request, jsonify
from app import app
from SQLcon import *


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello, world!'


@app.route('/get_messages', methods=['POST'])
def get_all_messages():
    page = request.form.get('page')
    data = get_messages(page)
    return {'data': data}


@app.route('/add_message', methods=['POST'])
def add_msg():
    name = request.form.get('username')
    msg = request.form.get('message')
    page = request.form.get('page')
    if name and msg:
        add_message(name, msg, page)
        return {'status': True}
    return {'status': False, 'warn': 'строки не должны быть пустыми'}
