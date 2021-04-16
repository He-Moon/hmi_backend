# -*- coding: utf-8 -*-
from app import db


class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    msg_type = db.Column(db.String(10), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    zh_msg = db.Column(db.String(100), nullable=False)
    en_msg = db.Column(db.String(100), nullable=False)
    zh_tip = db.Column(db.String(100), default='请联系开发人员')
    en_tip = db.Column(db.String(100), default='connect evelopers')
    timeout = db.Column(db.Integer, default=None)
    timestamp = db.Column(db.Integer, nullable=False)
