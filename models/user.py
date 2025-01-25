from db import db


class UserModel(db.Model):
    __tablename__ = "users"
    # Required fields to create a user
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
