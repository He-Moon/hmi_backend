# -*- coding: utf-8 -*-
from flask import request
from flask_restful import Resource
from app.validators.log import LogSchema
from app.common.response import format_res

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
        # ws_res = requesting.send_log_message(data)
        #
        # if ws_res:
        #     std_res = GET_STD_RES()
        # else:
        #     std_res = GET_STD_RES(code=-1)
        # return std_res

    def get(self):
        print self
        return 'start'
