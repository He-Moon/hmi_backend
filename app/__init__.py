from flask import Flask
from flask_socketio import SocketIO

from app.models.log import db

app = Flask(__name__)
app.config.from_object('app.secure')
app.config.from_object('app.setting')
socketio = SocketIO(app, cors_allowed_origins="*")

from app.web import web

app.register_blueprint(web)

db.init_app(app)
db.create_all(app=app)


@socketio.on('connect')
def establish_sockio():
    print 'socket connect'


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')
