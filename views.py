from flask import render_template, request, jsonify, url_for, send_from_directory, session
from app import app
from SQLcon import *
import config


@app.route('/')
def hello_world():
    return 'Hello, world!'


@app.route('/login', methods=['GET'])
def login_get():
    if session.get('login') == config.key_login:
        return {'status': True}
    return {'status': False}


@app.route('/login', methods=['POST'])
def login_set():
    login = request.form.get('login')
    psw = request.form.get('psw')
    if login == config.app_login and psw == config.app_password:
        session['login'] = config.key_login
        return {'status': True}
    return {'status': False}


@app.route('/get_messages', methods=['POST'])
def get_all_messages():
    page = request.form.get('page')
    data = get_messages(page)
    return {'data': data}


@app.route('/get_items', methods=['GET'])
def get_shop_items():
    data = get_items()
    return {'data': data}


@app.route('/get_item/<string:item_id>', methods=['GET'])
def get_shop_item(item_id):
    data = get_item(item_id)
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


@app.route('/add_item', methods=['POST'])
def add_new_item():
    if session.get('login') == config.key_login:
        item_name = request.form.get('item_name')
        item_description = request.form.get('item_description')
        item_price = request.form.get('item_price')
        img_name = request.form.get('img_name')
        count = request.form.get('count')
        if item_name and item_description and item_price and img_name and count:
            add_item(item_name, item_description, int(item_price), img_name, int(count))
            return {'status': True}
    return {'status': False}


@app.route('/delete_item', methods=['POST'])
def delete_item_id():
    if session.get('login') == config.key_login:
        item_id = request.form.get('itemID')
        delete_item(int(item_id))
        return {'status': True}
    return {'status': False}


@app.route('/get_img/<string:img>')
def get_img(img):
    return send_from_directory('static/img', f'{img}.jpg')
