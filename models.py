import os
from sqlalchemy import Column, String, Integer, create_engine
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql.sqltypes import Date

DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '1234')
DB_NAME = os.getenv('DB_NAME', 'csce002')
DB_PATH = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(database_path=DB_PATH):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

    migrate = Migrate(app, db)


'''
Student

'''


class Student(db.Model):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    university_id = Column(Integer)
    name = Column(String)
    password = Column(String)
    permissions = Column(String)
    noPosts = Column(Integer)
    gpa = Column(String)
    courses = Column(String)  # String List
    grade = Column(Integer)
    birthday = Column(Date)
    email = Column(String)
    schedule = Column(String)

    def __init__(self, university_id, name, password, permissions, noPosts, gpa, courses, grade, birthday, email):
        self.university_id = university_id
        self.name = name
        self.password = password
        self.permissions = permissions
        self.noPosts = noPosts
        self.gpa = gpa
        self.courses = courses
        self.grade = grade
        self.birthday = birthday
        self.email = email

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'university_id': self.university_id,
            'name': self.name,
            'password': self.password,
            'permissions': self.permissions,
            'noPosts': self.noPosts,
            'gpa': self.gpa,
            'courses': self.courses,
            'grade': self.grade
        }


'''
Requests

'''


class Request(db.Model):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True)
    stuID = Column(Integer)
    stuName = Column(String)
    email = Column(String)
    coursecode = Column(String)
    topic = Column(String)
    req_type = Column(String)
    date = Column(String)

    def __init__(self, stuID, stuName, email, coursecode, topic, req_type, date):
        self.stuID = stuID
        self.stuName = stuName
        self.email = email
        self.coursecode = coursecode
        self.topic = topic
        self.req_type = req_type
        self.date = date

    def format(self):
        return {
            'id': self.id,
            'stuID': self.stuID,
            'stuName': self.stuName,
            'email': self.email,
            'coursecode': self.coursecode,
            'topic': self.topic,
            'req_type': self.req_type,
            'date': self.date
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Official_Request(db.Model):
    __tablename__ = 'official_requests'

    id = Column(Integer, primary_key=True)
    stuID = Column(Integer)
    stuName = Column(String)
    email = Column(String)
    title = Column(String)
    body = Column(String)
    date = Column(String)

    def __init__(self, stuID, stuName, email, title, body, date):
        self.stuID = stuID
        self.stuName = stuName
        self.email = email
        self.title = title
        self.body = body
        self.date = date

    def format(self):
        return {
            'id': self.id,
            'stuID': self.stuID,
            'stuName': self.stuName,
            'email': self.email,
            'title': self.title,
            'body': self.body,
            'date': self.date
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


'''
Course

'''


class Course(db.Model):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    resources = Column(String)  # String List
    session_dates = Column(String)  # String List
    announcements = Column(String)

    def __init__(self, name, resources, session_dates, announcements):
        self.name = name
        self.resources = resources
        self.session_dates = session_dates
        self.announcements = announcements

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'resources': self.resources,
            'session_dates': self.session_dates,
            'announcements': self.announcements,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


setup_db()
