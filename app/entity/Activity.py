
from app import db
from app.entity.Entity import Entity


class Activity(Entity, db.Model):

    __tablename__ = "activities"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.Text)

    user = db.relationship('User', back_populates="activities")

    def __init__(self,description,user_id):
        Entity.__init__(self)
        self.description=description
        self.user_id=user_id
