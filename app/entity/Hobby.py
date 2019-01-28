
from app import db
from app.entity.Entity import Entity


class Hobby(Entity, db.Model):

    __tablename__ = "hobbies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(190), nullable=False)
    icon = db.Column(db.String(190), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.Text)

    user = db.relationship('User', back_populates="hobbies")
