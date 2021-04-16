import os
import time

module_base = os.path.dirname(os.path.abspath(__file__)) + '/../'


def format_date():
    time_now = int(time.time())
    time_local = time.localtime(time_now)
    date = time.strftime("%y_%m_%d", time_local)
    return date

