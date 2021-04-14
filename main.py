# -*- coding: utf-8 -*-
from flask_socketio import SocketIO
from app import create_app

app = create_app()
socketio = SocketIO(app, cors_allowed_origins="*")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port='4000', debug=app.config['DEBUG'])
    # 生产环境的服务启动： nginx + uwsgi
