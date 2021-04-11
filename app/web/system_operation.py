from flask import request

from . import web


@web.route('/start')
def start():
    return request.args['q']
