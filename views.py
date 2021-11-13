from flask import render_template, request, jsonify, url_for, send_from_directory
from app import app
from SQLcon import *


@app.route('/')
def hello_world():
    return 'Hello, world!'


@app.route('/get_messages', methods=['POST'])
def get_all_messages():
    page = request.form.get('page')
    data = get_messages(page)
    return {'data': data}


@app.route('/get_items', methods=['GET'])
def get_shop_items():
    data = get_items()
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
    item_name = request.form.get('item_name')
    item_description = request.form.get('item_description')
    item_price = request.form.get('item_price')
    img_name = request.form.get('img_name')
    count = request.form.get('count')
    add_item(item_name, item_description, item_price, img_name, count)
    return {'status': True}


@app.route('/get_img/<string:img>')
def get_img(img):
    return send_from_directory('static/img', f'{img}.jpg')
