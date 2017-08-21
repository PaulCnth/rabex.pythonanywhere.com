# -*- coding: utf-8 -*-
"""
                miniblog
                ~~~~~~~~

        1. 使用falsk创建微博应用
        2. 使用模版以求代码重用
        3. 登陆退出功能，登陆认证界面
        4. 管理界面
        5. 使用sqlite3数据库存储
        6. SqlAlchemy建立orm数据库模型

"""
from flask import Flask, render_template, redirect, url_for, request, session, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from uuid import uuid4
import os


app = Flask(__name__)
app.debug = True
app.config.update(dict(
    SECRET_KEY=str(uuid4()),
    USERNAME='admin',
    PASSWORD='ADMIN',
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(os.getcwd(), 'miniblog.db'),

    # 以下为debugtoolbar的选项
    DEBUG_TB_ENABLED=app.debug, # 启用工具栏
    # DEBUG_TB_HOSTS=[], # 显示工具栏的host白名单
    DEBUG_TB_INTERCEPT_REDIRECTS=False, # 要拦截重定向？
    # DEBUG_TB_PANELS=[], # 面板的模版、类名的清单
    DEBUG_TB_PROFILER_ENABLED=False, # 启用所有请求的分析工具
    DEBUG_TB_TEMPLATE_EDITOR_ENABLED=True, # 启用模版编辑器

))
db = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)


class Entries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return '<Title: %r>' % self.title


@app.route('/')
def show_entries():
    entries = Entries.query.all()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    entry = Entries(title=request.form['title'], text=request.form['text'])
    db.session.add(entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('.show_entries'))


@app.route('/path')
def app_path():
    return """root_path=%r <br>request.endpoint=%r <br>url_for=%r""" % (app.root_path, request.endpoint, url_for('show_entries') )
@app.route('/create_all')
def create_all():
    db.create_all()
    return 'done..:-)'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
