from sqlalchemy import Column
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'USERS'

    user_id = Column(db.String(20), primary_key=True)
    user_pw = Column(db.String(40), nullable=False)
    signup_time = Column(db.DateTime, default=datetime.now)
    stay = Column(db.String(1), nullable=False, default=0)
    goingout = Column(db.String(1), nullable=False, default=0)


db.create_all()
# 모든 model 생성

