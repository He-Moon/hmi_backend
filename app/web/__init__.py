from flask import Blueprint
from flask_restful import Api, Resource
from flask_cors import CORS

web = Blueprint('web', __name__)
from app.web import system_operation
from app.web import vision
from app.web import user

CORS(web)
api = Api(web)


class Alive(Resource):
    def get(self):
        return {'echo': 'alive'}


"""
alive
"""

api.add_resource(Alive, '/')

"""
system_operation
"""
api.add_resource(system_operation.Start, '/api/cmd/start')
api.add_resource(system_operation.Stop, '/api/cmd/stop')
api.add_resource(system_operation.Pause, '/api/cmd/pause')
api.add_resource(system_operation.Continue, '/api/cmd/restart')

"""
vision
"""
api.add_resource(vision.VisionTopics, '/vision/topics')
