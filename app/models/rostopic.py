from sqlalchemy import Column, String, Integer, Boolean
from ..db_1 import db


class VisionRostopic(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    topic = Column(String(30), nullable=False)
    type = Column(String(), nullable=False)
    isUsed = Column(Boolean, nullable=False, default=False)

