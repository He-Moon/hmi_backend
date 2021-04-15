# -*- coding: utf-8 -*-
from flask_restful import Resource
from app.common.response import format_res

"""
todo
初始化所有节点
单个节点启动
停止所有节点
停止单个节点
....
"""


class Node(Resource):
    def __init__(self):
        pass

    def get(self):
        return format_res()
