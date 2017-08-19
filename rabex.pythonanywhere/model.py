# -*- coding: utf-8 -*-
from run import db
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Book(db.Model):
    """
    书籍列表
    一个作者可有多本书
    一本书可由多个作者合著
    many-to-many
    """
    __tablename__ = 'scl_book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship('Author', backref=db.backref('books', lazy='dynamic'))
    press = db.Column(db.String(30), nullable=False)
    pub_date = db.Column(db.DateTime)
    isbn = db.Column(db.String(30))

    def __init__(self, name, author, press, pub_date, isbn):
        self.name = name
        self.author = author
        self.press = press
        if pub_date is None:
            self.pub_date = datetime.date.today()
        self.pub_date = pub_date
        self.isbn = isbn

    def __repr__(self):
        return '<Book %r by %r>' % (self.name, self.author)


class Author(db.Model):
    """
    作者列表
    """
    __tablename__ = 'scl_author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.Boolean, ) # 1=male,0=female
    age = db.Column(db.Integer)
    location = db.Column(db.String(120))

    def __init__(self, name, age, location, gender=None):
        self.name = name
        self.age = age
        self.location = location
        if gender is None:
            self.gender = True
        self.gender = gender

    def __repr__(self):
        return '<Author %r>' % self.name

# 多对多关系表，文档中这样介绍：
# If you want to use many-to-many relationships you will need to define a helper table
# that is used for the relationship. For this helper table it is strongly recommended to
# not use a model but an actual table:
authors = db.Table(
    'authors',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)
