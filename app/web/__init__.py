from flask import Blueprint
from flask_restful import Api, Resource
from flask_cors import CORS

web = Blueprint('web', __name__)
from app.web import system_operation, vision, connect, log, user, config_file

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
api.add_resource(system_operation.Reset, '/api/cmd/reset')
api.add_resource(system_operation.Shutdown, '/api/cmd/shutdown')

"""
connect
"""
api.add_resource(connect.Connect, '/connect_status')

"""
log
"""
api.add_resource(log.Logs, '/api/notify/system_log')
api.add_resource(log.QueryLog, '/api/query/log')
"""
vision
"""
api.add_resource(vision.VisionTopicsList, '/vision/topics_list')
api.add_resource(vision.VisionTopics, '/vision/topics')

"""
config_file
"""
api.add_resource(config_file.ProjectConfigFile, '/config_file')
