from app import db


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __init__(self, user, msg):
        self.username = user
        self.message = msg


def add_message(user, msg):
    message = Messages(user, msg)
    db.session.add(message)
    db.session.commit()
    return message


def get_messages():
    msg = Messages.query.all()[-50::]
    return [{'id': i.id, 'name': i.username, 'message': i.message}for i in msg]
