from flask import Blueprint
from flask_restful import Api

web = Blueprint('web', __name__)

from app.web import system_operation
from app.web import vision
from app.web import user

api = Api(web)
"""
system_operation
"""
api.add_resource(system_operation.Start, '/start')
api.add_resource(system_operation.Stop, '/stop')
api.add_resource(system_operation.Pause, '/pause')
api.add_resource(system_operation.Continue, '/continue')

"""
vision
"""
api.add_resource(vision.VisionTopics, '/vision/topics')
