from app import socketio


def send_log_by_websocket(data):
    try:
        socketio.emit('system_log', data)
        # todo print/log info
        return True
    except Exception as e:
        print e
        # todo print/log error
        return False


def send_connect_status_by_websocket(data):
    try:
        socketio.emit('connect_status', data)
        print data
        return True
    except Exception as e:
        print e
        return False
