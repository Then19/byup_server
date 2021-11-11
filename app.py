from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dev:admin@localhost/online_chat'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)


if __name__ == '__main__':
    from views import *
    app.run()
