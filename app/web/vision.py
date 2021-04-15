# -*- coding: utf-8 -*-
# 获取rostopic list / 以及 type 数据处理后返回给前端
from flask_restful import Resource
from app.common.rostopic import getRostopics
from app.common.response import format_res


def format_topic(topic_data):
    return {'topic': topic_data[0], 'type': topic_data[1]}


class VisionTopicsList(Resource):
    def __init__(self):
        pass

    def get(self):
        """
        获取topic list 列表
        :return:
        """
        topic_list = [format_topic(topic) for topic in getRostopics()]
        return format_res(code=0, data=topic_list)


class VisionTopics(Resource):

    def __init__(self):
        pass

    def get(self):
        """
        获取已经保存的topic
        :return:
        """
        return format_res()

    def post(self):
        """
        提交需要保存的topic
        :return:
        """
        return format_res()
