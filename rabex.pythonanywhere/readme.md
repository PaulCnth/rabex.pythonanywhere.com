# [rabex.pythonanywhere.com](rabex.pythonanywhere.com)

这是托管在 [pythonanywhere](https://www.pythonanywhere.com) 上的一个`flask`项目。

0818-0856
---------
首先创建虚拟环境，这里使用的是windows平台下的`virtualenv==15.1.0`。
创建虚拟环境的方式很简单，就一句话：

> virtualenv -p c:\Python27\python.exe py2k

其中`-p`选项是指定索要使用的python解析器路径。`py2k`是一个你便于记忆的环境目录名。
windows中是进入运行 `py2k\Scriptactivate`，就进入了虚拟环境，linux中bash环境下则必须使用 `source lib/activate` 命令进入。
接着我们安装需要的 _packages & modules_.
虚拟环境中我们使用pip安装。

> pip install flask flask-login flask-assets flask-debugtoolbar flask-wtf flask-cache flask-admin flask-restful flask-restless flask-babel flask-security flask-limiter flask-sqlalchemy  

```
aniso8601==1.2.1
Babel==2.4.0
blinker==1.4
click==6.7
Flask==0.12.2
Flask-Admin==1.5.0
Flask-Assets==0.12
Flask-Babel==0.11.2
Flask-BabelEx==0.9.3
Flask-Cache==0.13.1
Flask-DebugToolbar==0.10.1
Flask-Limiter==0.9.5
Flask-Login==0.4.0
Flask-Mail==0.9.1
Flask-Principal==0.4.0
Flask-RESTful==0.3.6
Flask-Restless==0.17.0
Flask-Security==3.0.0
Flask-SQLAlchemy==2.2
Flask-WTF==0.14.2
itsdangerous==0.24
Jinja2==2.9.6
limits==1.2.1
MarkupSafe==1.0
mimerender==0.6.0
passlib==1.7.1
python-dateutil==2.6.1
python-mimeparse==1.6.0
pytz==2017.2
six==1.10.0
speaklater==1.3
SQLAlchemy==1.1.13
webassets==0.12.1
Werkzeug==0.12.2
WTForms==2.1
```

上述这些相互依赖的包安装完毕，就搭建好平台了，可以开始开发了。
**happy coding!!!**
