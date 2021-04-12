def FORMAT_RES(code=0, msg='success', data=True):
    if code == 0:
        res = {
            'code': code,
            'msg': msg,
            'data': data
        }
    else:
        res = {}
        pass
    return res
