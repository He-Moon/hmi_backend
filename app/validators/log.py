from marshmallow import Schema, fields


class LogSchema(Schema):
    msg_type = fields.String()  # 'error', 'info'
    code = fields.String()  # 'W0001', ...
    en_msg = fields.String(missing='', default='')  # 'Dropped SKU', 'Nonconform SKU', ...
    zh_msg = fields.String()
    en_tip = fields.String(missing='', default='')
    zh_tip = fields.String(missing='', default='')
    timeout = fields.Int(missing=None, default=None)


class QueryLogSchema(Schema):
    date = fields.String()
