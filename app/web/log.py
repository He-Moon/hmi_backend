# -*- coding: utf-8 -*-
from flask import request
from flask_restful import Resource
from app.validators.log import LogSchema, QueryLogSchema
from app.common.response import format_res
from app.common.util import format_unicode_data, trans_timestamp, today_timestamp
from app.common.socket import send_log_by_websocket
from app.models.log import Log
from app import db
import time


class Logs(Resource):

    def __init__(self):
        pass

    def post(self):
        log_schema = LogSchema()
        data, error = log_schema.loads(request.data)
        if error:
            msg = 'data type error'
            res = format_res(code=-1, msg=msg)
            return res

        timestamp = today_timestamp()
        data['timestamp'] = timestamp
        self.save_to_db(data)
        ws_res = send_log_by_websocket(data)
        if ws_res:
            return format_res()
        else:
            return format_res(code=-1)

    @staticmethod
    def save_to_db(data):
        # data = format_unicode_data(data)
        log = Log(
            msg_type=data['msg_type'],
            code=data['code'],
            zh_msg=data['zh_msg'],
            en_msg=data['en_msg'],
            zh_tip=data['zh_tip'],
            en_tip=data['en_tip'],
            timeout=data['timeout'],
            timestamp=data['timestamp']
        )
        db.session.add(log)
        db.session.commit()


class QueryLog(Resource):
    def __init__(self):
        pass

    def post(self):
        query_log_schema = QueryLogSchema()
        data, error = query_log_schema.load(request.get_json())
        req_data = self.get_data_from_db(data)
        if error:
            msg = 'data type error'
            res = format_res(code=-1, msg=msg)
            return res
        return format_res(data=req_data)

    @staticmethod
    def get_data_from_db(data):
        error_logs = Log.query.filter_by(timestamp=trans_timestamp(data['date'])).filter_by(msg_type='error')
        error_logs = [log.to_dict() for log in error_logs]

        warning_logs = Log.query.filter_by(timestamp=trans_timestamp(data['date'])).filter_by(msg_type='warning')
        warning_logs = [log.to_dict() for log in warning_logs]

        info_logs = Log.query.filter_by(timestamp=trans_timestamp(data['date'])).filter_by(msg_type='info')
        info_logs = [log.to_dict() for log in info_logs]

        return {'errors': error_logs, 'warns': warning_logs, 'infos': info_logs}
