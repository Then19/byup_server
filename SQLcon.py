from app import db


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
    page = db.Column(db.VARCHAR(50), nullable=False)

    def __init__(self, user, msg, page):
        self.username = user
        self.message = msg
        self.page = page


def add_message(user, msg, page):
    message = Messages(user, msg, page)
    db.session.add(message)
    db.session.commit()
    return message


def get_messages(page):
    msg = Messages.query.filter_by(page=page).all()[-75::]
    return [{'id': i.id, 'name': i.username, 'message': i.message}for i in msg]


if __name__ == "__main__":
    db.create_all()
