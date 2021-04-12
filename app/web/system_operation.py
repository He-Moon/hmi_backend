from flask_restful import Resource


class Start(Resource):

    def __init__(self):
        pass

    def get(self):
        print self
        return 'start'


class Stop(Resource):

    def __init__(self):
        pass

    def get(self):
        print self
        return 'stop'


class Continue(Resource):

    def __init__(self):
        pass

    def get(self):
        print self
        return 'continue'


class Pause(Resource):

    def __init__(self):
        pass

    def get(self):
        print self
        return 'pause'
