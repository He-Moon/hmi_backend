# -*- coding: utf-8 -*-
import subprocess
from flask_restful import Resource
from app.common.response import format_res


# todo 读取对应路径的脚本。

class Start(Resource):

    def __init__(self):
        pass

    def get(self):
        try:
            subprocess.check_call(['python /home/xyz/start.py'])
            return format_res()
        except Exception as e:
            print type(e)
            return format_res(code=-1)


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
        try:
            subprocess.check_call(['systemctl poweroff -i'])
        except Exception as e:
            print e
            return format_res(code=-1)
