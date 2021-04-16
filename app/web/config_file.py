# -*- coding: utf-8 -*-
from flask import request
import os
import json
from flask_restful import Resource
from app.common.response import format_res
from app.common.util import module_base


class ProjectConfigFile(Resource):
    def __init__(self):
        self.project_config_path = module_base + 'configs/project_config.json'
        pass

    def get(self):
        if os.path.exists(self.project_config_path):
            with open(self.project_config_path, 'r') as f:
                project_config_file = json.load(f)
        else:
            project_config_file = {}
        return format_res(data=project_config_file)

    def post(self):
        with open(self.project_config_path, 'w') as f:
            json.dump(request.get_json(), f, indent=4)

        return format_res()
