# -*- coding: utf-8 -*-
# 获取rostopic list / 以及 type 数据处理后返回给前端
from flask_restful import Resource
from app.common.rostopic import getRostopics
from app.common.response import format_res
import os
from app.common.util import module_base
import json


def format_topic(topic_data):
    return {'topic': topic_data[0], 'type': topic_data[1], 'subscribed': False}


class VisionTopics(Resource):

    def __init__(self):
        self.rostopic_config_path = module_base + 'configs/rostopic_config.json'
        pass

    def get(self):
        """
        获取已经保存的topic
        :return:
        """
        if os.path.exists(self.rostopic_config_path):
            with open(self.rostopic_config_path, 'r') as f:
                self.topic_list = json.load(f)['topic_list']
        else:
            self.topic_list = [format_topic(topic) for topic in getRostopics()]
            with open(self.rostopic_config_path, 'w') as f:
                topic_list = {
                    'topic_list': self.topic_list
                }
                json.dump(topic_list, f, indent=4)

        return format_res(code=0, data=self.topic_list)

    def post(self):
        """
        提交需要保存的topic
        :return:
        """
        return format_res()
