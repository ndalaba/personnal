from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import profils
from . import educations
from . import jobs
from . import services
from . import hobbies
from . import skills
from . import works
from . import messages
