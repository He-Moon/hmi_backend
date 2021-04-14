from marshmallow import Schema, fields


class LogSchema(Schema):
    msg_type = fields.String()  # 'error', 'info'
    code = fields.String()  # 'W0001', ...
    en_msg = fields.String(missing=None, default=None)  # 'Dropped SKU', 'Nonconform SKU', ...
    zh_msg = fields.String()
    en_tip = fields.String(missing=None, default=None)
    zh_tip = fields.String()
    timeout = fields.Int(missing=None, default=None)
