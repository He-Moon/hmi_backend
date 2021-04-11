from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import system_operation
from app.web import user
