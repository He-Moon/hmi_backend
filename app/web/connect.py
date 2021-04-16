# -*- coding: utf-8 -*-
from flask_restful import Resource
from app.common.response import format_res
from app.common.socket import send_connect_status_by_websocket



class Connect(Resource):
    def __init__(self):
        pass

    def post(self):
        mock_data = [
            {
                "name": "plc",
                "status": True
            }
        ]
        send_connect_status_by_websocket(mock_data)
        return format_res()
