from . import db
from flask_login import UserMixin,current_user
from sqlalchemy.sql import func
from datetime import datetime

####################################
from flask import jsonify
###################################



group_membership = db.Table('group_membership',
                            db.Column('group_id',db.Integer,db.ForeignKey('group.id'),primary_key=True),
                            db.Column('user_id',db.Integer,db.ForeignKey('user.id'),primary_key = True),
                            db.Column('is_admin', db.Boolean, default=False)
                            )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    nickname = db.Column(db.String(150), unique=True)
    groups = db.relationship('Group', secondary=group_membership, backref=db.backref('users', lazy='dynamic'))
    task = db.relationship('Task',backref='user')

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    code = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(200), nullable = True)
























class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start = db.Column(db.DateTime,nullable = True)
    end = db.Column(db.DateTime,nullable = True)
    description = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)




    

#####################################################
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'start': self.start.isoformat(),
            'end': self.end.isoformat() if self.end else None
        }




