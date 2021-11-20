from app import db
import datetime


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
    page = db.Column(db.VARCHAR(50), nullable=False)
    date_time = db.Column(db.VARCHAR(50), nullable=False)

    def __init__(self, user, msg, page, date_time):
        self.username = user
        self.message = msg
        self.page = page
        self.date_time = date_time


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(150), nullable=False)
    item_description = db.Column(db.Text, nullable=False)
    item_price = db.Column(db.Integer, nullable=False)
    img_name = db.Column(db.VARCHAR(50), nullable=False)
    count = db.Column(db.Integer, nullable=False)

    def __init__(self, item_name, item_description, item_price, img_name, count):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.img_name = img_name
        self.count = count


class Offers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_firstname = db.Column(db.String(50), nullable=False)
    user_lastname = db.Column(db.String(50), nullable=False)
    user_number = db.Column(db.String(50), nullable=False)
    user_address = db.Column(db.String(150), nullable=False)
    user_comment = db.Column(db.Text, nullable=False)
    offer_items = db.Column(db.String(150), nullable=False)

    def __init__(self, user_firstname, user_lastname, user_number, user_address, user_comment, offer_items):
        self.user_firstname = user_firstname
        self.user_lastname = user_lastname
        self.user_number = user_number
        self.user_address = user_address
        self.user_comment = user_comment
        self.offer_items = offer_items


def add_message(user, msg, page):
    date_time = datetime.datetime.now().strftime("%Y/%m/%d %H.%M.%S")
    message = Messages(user, msg, page, date_time)
    db.session.add(message)
    db.session.commit()
    return message


def get_messages(page):
    msg = Messages.query.filter_by(page=page).all()[-75::]
    return [{'id': i.id, 'name': i.username, 'message': i.message, 'time': i.date_time} for i in msg]


def get_items():
    item = Items.query.all()
    return [{'id': i.id, 'item_name': i.item_name, 'item_description': i.item_description, 'item_price': i.item_price,
             'img_name': i.img_name, 'count': i.count} for i in item]


def get_item(item_id):
    item = Items.query.filter_by(id=item_id).all()
    return [{'id': i.id, 'item_name': i.item_name, 'item_description': i.item_description, 'item_price': i.item_price,
             'img_name': i.img_name, 'count': i.count} for i in item]


def add_item(item_name, item_description, item_price, img_name, count):
    item = Items(item_name, item_description, item_price, img_name, count)
    db.session.add(item)
    db.session.commit()
    return item


def add_new_offer(user_firstname, user_lastname, user_number, user_address, user_comment, offer_items):
    offer = Offers(user_firstname, user_lastname, user_number, user_address, user_comment, offer_items)
    db.session.add(offer)
    db.session.commit()
    return offer


def delete_item(item_id):
    Items.query.filter_by(id=item_id).delete()
    db.session.commit()


if __name__ == "__main__":
    db.create_all()
