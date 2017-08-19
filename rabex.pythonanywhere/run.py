# -*- coding: utf-8 -*-
"""

        run.py是应用的入口文件

1. model
    数据库及其表，关系创建文件

2. view
    将数据库查询数据，发送到templates模版内response到前端展示

3. Templates/*
    该文件夹下文件为view对应的模版文件

"""
from flask import Flask, render_template, g, session, redirect
from uuid import uuid4
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
# from model import User, Post, Category, Book, Author

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = str(uuid4())
# toolbar = DebugToolbarExtension(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'rabex.db')
db = SQLAlchemy(app)


@app.route('/')
@app.route('/<string:user>')
def hello(user=None):
    return render_template('layout.html', user=user)


if __name__ == '__main__':
    app.run()
