import os
import time, datetime
import json

module_base = os.path.dirname(os.path.abspath(__file__)) + '/../'


def today_timestamp():
    return int(time.mktime(datetime.date.today().timetuple()))


def trans_timestamp(date_str):
    time_array = time.strptime(date_str, "%Y_%m_%d")
    timestamp = time.mktime(time_array)
    return int(timestamp)


def format_unicode_data(data):
    if isinstance(data, str):
        data = json.loads(data)
    for key in data:
        if isinstance(data[key], unicode):
            data[key] = json.dumps(data[key], encoding='utf-8', ensure_ascii=True)
    return data
