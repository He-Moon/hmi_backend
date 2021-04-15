# -*- coding: utf-8 -*-
from flask_restful import Resource
from app.common.response import format_res


# todo 读取对应路径的脚本。

class Start(Resource):

    def __init__(self):
        pass

    def get(self):
        return format_res()


class Stop(Resource):

    def __init__(self):
        pass

    def get(self):
        return format_res()


class Continue(Resource):

    def __init__(self):
        pass

    def get(self):
        return format_res()


class Pause(Resource):

    def __init__(self):
        pass

    def get(self):
        return format_res()


class Reset(Resource):

    def __init__(self):
        pass

    def get(self):
        return format_res()


class Shutdown(Resource):

    def __init__(self):
        pass

    def get(self):
        return format_res()
