# -*- coding: utf-8 -*-

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4000', debug=app.config['DEBUG'])
    # 生产环境的服务启动： nginx + uwsgi
