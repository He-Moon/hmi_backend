from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

db = SQLAlchemy()


class Log(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(5), nullable=False)
    zh_msg = Column(String(100), nullable=False)
    zh_tip = Column(String(100), default='connect evelopers')
