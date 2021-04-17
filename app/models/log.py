# -*- coding: utf-8 -*-
from app import db


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


db.Model.to_dict = to_dict
db.Model.__table_args__ = {
    "mysql_charset": "utf8"
}


class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    msg_type = db.Column(db.String(10))
    code = db.Column(db.String(10))
    zh_msg = db.Column(db.String(100))
    en_msg = db.Column(db.String(100))
    zh_tip = db.Column(db.String(100))
    en_tip = db.Column(db.String(100))
    timeout = db.Column(db.Integer)
    timestamp = db.Column(db.Integer)
