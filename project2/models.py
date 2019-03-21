"""
Database models
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project2 import db, login_manager, marshmallow, Base
from flask_login import UserMixin
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin
import json


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin, Base):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    profile_image = db.Column(
        db.String(20),
        nullable=False,
        default='user_profile.png')
    password = db.Column(db.String(60), nullable=True)
    courses = db.relationship('Course', backref='author', lazy=True)
    categories = db.relationship('Category', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.user_name}', '{self.email}', '{self.image_file}')"


class OAuth (db.Model, OAuthConsumerMixin, Base):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    courses = db.relationship(User)


class Category(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    courses = db.relationship('Course', backref='category', lazy=True)


class Course(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer)
    Category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class CourseSchema(marshmallow.ModelSchema):
    class Meta:
        model = Course


class CategorySchema(marshmallow.ModelSchema):
    class Meta:
        model = Category
        courses = marshmallow.Nested(CourseSchema, many=True)
