# Base Entity

from datetime import datetime
<<<<<<< HEAD
from sqlalchemy import Column, String, DateTime, event
=======
from sqlalchemy import Column, String, DateTime, event, Boolean
>>>>>>> ee6c30bbb9ffcfc4922c4a1ed46307d23ffecb99
from app.utils.str_helper import generate_uuid

class Entity(object):

<<<<<<< HEAD
    uid = Column(String(30),index=True,unique=True,nullable=False, default=generate_uuid(8))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
=======
    uid = Column(String(30),index=True,unique=True,nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    published = Column(Boolean, default=False)

    def __init__(self):
        self.uid=generate_uuid(5)
>>>>>>> ee6c30bbb9ffcfc4922c4a1ed46307d23ffecb99
    
    @staticmethod
    def _updated_at(mapper, connection, target):
        target.updated_at = datetime.utcnow()

    @classmethod
    def __declare_last__(cls):
        event.listen(cls, 'before_update', cls._updated_at)
