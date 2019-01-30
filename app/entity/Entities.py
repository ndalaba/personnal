
from app import db
from app.entity.Entity import Entity


class Work(Entity, db.Model):

    __tablename__ = "works"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(190), nullable=False)
    techno = db.Column(db.String(190), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.Text)
    url = db.Column(db.String(190))
    image= db.Column(db.String(190))

    user = db.relationship('User', back_populates="works")

class Skill(Entity, db.Model):

    __tablename__ = "skills"

    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(190), nullable=False)
    level = db.Column(db.String(190), nullable=False)
    experience = db.Column(db.Integer)
    percent = db.Column(db.Integer)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates="skills")

class Service(Entity, db.Model):

    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(190), nullable=False)
    icon = db.Column(db.String(190))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.Text)
    detail=db.Column(db.Text)

    user = db.relationship('User', back_populates="services")

class Job(Entity, db.Model):

    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(190), nullable=False)
    location = db.Column(db.String(190), nullable=False)
    company = db.Column(db.String(190), nullable=False)
    begin = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.Text)

    user = db.relationship('User', back_populates="jobs")

class Hobby(Entity, db.Model):

    __tablename__ = "hobbies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(190), nullable=False)
    icon = db.Column(db.String(190), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.Text)

    user = db.relationship('User', back_populates="hobbies")

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

class Education(Entity, db.Model):

    __tablename__ = "educations"

    id = db.Column(db.Integer, primary_key=True)
    formation = db.Column(db.String(190), nullable=False)
    location = db.Column(db.String(190), nullable=False)
    school = db.Column(db.String(190), nullable=False)
    begin = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.Text)

    user = db.relationship('User', back_populates="educations")