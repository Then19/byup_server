from flask import request, jsonify, send_from_directory
from app import app
from SQLcon import *
import config


@app.route('/')
def hello_world():
    return 'Hello, world!'


@app.route('/login', methods=['GET', 'POST'])
def login_get():
    login = request.form.get('login')
    psw = request.form.get('psw')
    status = False
    if login == config.app_login and psw == config.app_password:
        status = True
    resp = jsonify({'status': status})
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


@app.route('/get_messages', methods=['POST'])
def get_all_messages():
    page = request.form.get('page')
    response = jsonify({'data': get_messages(page)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_items', methods=['GET'])
def get_shop_items():
    data = get_items()
    response = jsonify({'data': data})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_item/<string:item_id>', methods=['GET'])
def get_shop_item(item_id):
    response = jsonify({'data': get_item(item_id)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/add_message', methods=['POST'])
def add_msg():
    name = request.form.get('username')
    msg = request.form.get('message')
    page = request.form.get('page')
    data = {'status': False, 'warn': 'строки не должны быть пустыми'}
    if name and msg:
        add_message(name, msg, page)
        data = {'status': True}
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/add_item', methods=['POST'])
def add_new_item():
    status = False
    login = request.form.get('login')
    psw = request.form.get('psw')
    if login == config.app_login and psw == config.app_password:
        item_name = request.form.get('item_name')
        item_description = request.form.get('item_description')
        item_price = request.form.get('item_price')
        img_name = request.form.get('img_name')
        count = request.form.get('count')
        if item_name and item_description and item_price and img_name and count:
            add_item(item_name, item_description, int(item_price), img_name, int(count))
            status = True
    resp = jsonify({'status': status})
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


@app.route('/delete_item', methods=['POST'])
def delete_item_id():
    status = False
    login = request.form.get('login')
    psw = request.form.get('psw')
    if login == config.app_login and psw == config.app_password:
        item_id = request.form.get('itemID')
        delete_item(int(item_id))
        status = True
    resp = jsonify({'status': status})
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


@app.route('/add_offer', methods=['POST'])
def add_offer():
    user_firstname = request.form.get('user_firstname', "")
    user_lastname = request.form.get('user_lastname', "")
    user_number = request.form.get('user_number', "")
    user_address = request.form.get('user_address', "")
    user_comment = request.form.get('user_comment', "")
    offer_items = request.form.get('offer_items', "")
    status = False
    if len(user_firstname) > 0 and len(user_lastname) and len(user_number) > 0 and len(user_address) > 0:
        if len(user_comment) == 0:
            user_comment = "Без комментариев"
        add_new_offer(user_firstname, user_lastname, str(user_number), user_address, str(user_comment), offer_items)
        status = True
    resp = jsonify({'status': status})
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


@app.route('/get_offers', methods=['GET'])
def get_offers_bot():
    if request.headers.get("bot_auth") == config.auth_bot:
        return jsonify(get_offers())
    return jsonify({'status': False})


@app.route('/get_img/<string:img>')
def get_img(img):
    return send_from_directory('static/img', f'{img}.jpg')
