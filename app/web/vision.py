# -*- coding: utf-8 -*-
# 获取rostopic list / 以及 type 数据处理后返回给前端
from flask_restful import Resource
from ..common import ros


class VisionTopics(Resource):

    def __init__(self):
        pass

    def get(self):
        types = ['Axes', 'Image', 'Marker', 'MarkerArray', 'PointCloud2', 'Pose', 'PoseArray', 'TF']
        print ros.getRostopics()
        return ros.getRostopics()
