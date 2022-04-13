from app import db

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), unique = True, index = True)
    password_hash = db.Column(db.String(128))
    reviews = db.relationship('Review', backref='reviewer', lazy = 'dynamic', cascade = "all, delete, delete-orphan")

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=False)
    address = db.Column(db.String(120), index=True, unique=False)
    num_reviews = db.Column(db.Integer, unique=False)
    sum_reviews = db.Column(db.Integer, unique=False)
    avg_rating = db.Column(db.Integer, index=True, unique=False)
    reviews = db.relationship('Review', backref = 'restaurant', lazy = 'dynamic', cascade = "all, delete, delete-orphan")

    def __repr__(self):
        return '<Restaurant {}>'.format(self.name)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column, automatically generated IDs
    rating = db.Column(db.Integer, unique = False) #a review's rating
    text = db.Column(db.String(200), unique = False) #a review's text
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id')) #foreign key column
    reviewer_id = db.Column(db.Integer, db.ForeignKey('user.id')) # another foreign key column

    def __repr__(self):
        return '<Review {}>'.format(self.text)
