# -*- coding: utf-8 -*-
def format_res(code=0, msg='success', zh_msg='成功', data=None):
    if code == 0:
        res = {
            'code': code,
            'msg': msg,
            'zh_msg': zh_msg,
            'data': data
        }
    elif code < 0:
        res = {
            'code': code,
            'msg': 'failure' if msg == 'success' else msg,
            'zh_msg': '失败' if msg == '成功' else zh_msg,
            'data': data
        }
    else:
        raise Exception('undefined code')

    return res
