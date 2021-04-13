from sqlalchemy import Column, String, Integer
from ..db import db


class Log(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(5), nullable=False)
    zh_msg = Column(String(100), nullable=False)
    zh_tip = Column(String(100), default='connect evelopers')
