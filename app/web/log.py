# -*- coding: utf-8 -*-
from flask import request
from flask_restful import Resource
from app.validators.log import LogSchema
from app.common.response import format_res
from app.common.socket import send_log_by_websocket


class Log(Resource):

    def __init__(self):
        pass

    def post(self):
        log_schema = LogSchema()
        data, error = log_schema.load(request.get_json())
        if error:
            msg = 'data type error'
            res = format_res(code=-1, msg=msg)
            return res

        # 存储到数据库
        # timestamp = time.time() * 1000
        # data['timestamp'] = timestamp
        ws_res = send_log_by_websocket(data)
        if ws_res:
            return format_res()
        else:
            return format_res(code=-1)

    def get(self):
        print self
        return 'start'
