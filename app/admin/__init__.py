from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import profils
from . import educations