# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer
from ..db import db


class Log(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    msg_type = Column(String(10), nullable=False)
    code = Column(String(5), nullable=False)
    zh_msg = Column(String(100), nullable=False)
    en_msg = Column(String(100), nullable=False)
    zh_tip = Column(String(100), default='请联系开发人员')
    en_tip = Column(String(100), default='connect evelopers')
    timeout = Column(Integer, default=None)
