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

> pip install flask flask-login flask-assets flask-debugtoolbar
              flask-wtf flask-cache flask-admin flask-restful
              flask-restless flask-babel flask-security
              flask-limiter flask-sqlalchemy

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

0818-0932
---------
### flaskr应用研究
#### flask app.config内置的设置区域

|Field|Description|
|:--|:--|
|DEBUG|	enable/disable debug mode
|TESTING|	enable/disable testing mode
|PROPAGATE_EXCEPTIONS|	explicitly enable or disable the propagation of exceptions. If not set or explicitly set to None this is implicitly true if either TESTING or DEBUG is true.|
|PRESERVE_CONTEXT_ON_EXCEPTION|	By default if the application is in debug mode the request context is not popped on exceptions to enable debuggers to introspect the data. This can be disabled by this key. You can also use this setting to force-enable it for non debug execution which might be useful to debug production applications (but also very risky).|
|SECRET_KEY|	the secret key|
|SESSION_COOKIE_NAME|	the name of the session cookie|
|SESSION_COOKIE_DOMAIN|	the domain for the session cookie. If this is not set, the cookie will be valid for all subdomains of SERVER_NAME.|
|SESSION_COOKIE_PATH|	the path for the session cookie. If this is not set the cookie will be valid for all of APPLICATION_ROOT or if that is not set for '/'.|
|SESSION_COOKIE_HTTPONLY|	controls if the cookie should be set with the httponly flag. Defaults to True.|
|SESSION_COOKIE_SECURE|	controls if the cookie should be set with the secure flag. Defaults to False.|
|PERMANENT_SESSION_LIFETIME|	the lifetime of a permanent session as datetime.timedelta object. Starting with Flask 0.8 this can also be an integer representing seconds.|
|SESSION_REFRESH_EACH_REQUEST|	this flag controls how permanent sessions are refreshed. If set to True (which is the default) then the cookie is refreshed each request which automatically bumps the lifetime. If set to False a set-cookie header is only sent if the session is modified. Non permanent sessions are not affected by this.|
|USE_X_SENDFILE|	enable/disable x-sendfile|
|LOGGER_NAME|	the name of the logger|
|LOGGER_HANDLER_POLICY|	the policy of the default logging handler. The default is 'always' which means that the default logging handler is always active. 'debug' will only activate logging in debug mode, 'production' will only log in production and 'never' disables it entirely.|
|SERVER_NAME|	the name and port number of the server. Required for subdomain support (e.g.: 'myapp.dev:5000') Note that localhost does not support subdomains so setting this to “localhost” does not help. Setting a SERVER_NAME also by default enables URL generation without a request context but with an application context.|
|APPLICATION_ROOT|	If the application does not occupy a whole domain or subdomain this can be set to the path where the application is configured to live. This is for session cookie as path value. If domains are used, this should be None.|
|MAX_CONTENT_LENGTH|	If set to a value in bytes, Flask will reject incoming requests with a content length greater than this by returning a 413 status code.|
|SEND_FILE_MAX_AGE_DEFAULT|	Default cache control max age to use with send_static_file() (the default static file handler) and send_file(), as datetime.timedelta or as seconds. Override this value on a per-file basis using the get_send_file_max_age() hook on Flask or Blueprint, respectively. Defaults to 43200 (12 hours).|
|TRAP_HTTP_EXCEPTIONS|	If this is set to True Flask will not execute the error handlers of HTTP exceptions but instead treat the exception like any other and bubble it through the exception stack. This is helpful for hairy debugging situations where you have to find out where an HTTP exception is coming from.|
|TRAP_BAD_REQUEST_ERRORS|	Werkzeug’s internal data structures that deal with request specific data will raise special key errors that are also bad request exceptions. Likewise many operations can implicitly fail with a BadRequest exception for consistency. Since it’s nice for debugging to know why exactly it failed this flag can be used to debug those situations. If this config is set to True you will get a regular traceback instead.|
|PREFERRED_URL_SCHEME|	The URL scheme that should be used for URL generation if no URL scheme is available. This defaults to http.|
|JSON_AS_ASCII|	By default Flask serialize object to ascii-encoded JSON. If this is set to False Flask will not encode to ASCII and output strings as-is and return unicode strings. jsonify will automatically encode it in utf-8 then for transport for instance.|
|JSON_SORT_KEYS|	By default Flask will serialize JSON objects in a way that the keys are ordered. This is done in order to ensure that independent of the hash seed of the dictionary the return value will be consistent to not trash external HTTP caches. You can override the default behavior by changing this variable. This is not recommended but might give you a performance improvement on the cost of cacheability.|
|JSONIFY_PRETTYPRINT_REGULAR|	If this is set to True (the default) jsonify responses will be pretty printed if they are not requested by an XMLHttpRequest object (controlled by the X-Requested-With header)|
|JSONIFY_MIMETYPE|	MIME type used for jsonify responses.|
|TEMPLATES_AUTO_RELOAD|	Whether to check for modifications of the template source and reload it automatically. By default the value is None which means that Flask checks original file only in debug mode.|
|EXPLAIN_TEMPLATE_LOADING|	If this is enabled then every attempt to load a template will write an info message to the logger explaining the attempts to locate the template. This can be useful to figure out why templates cannot be found or wrong templates appear to be loaded.|


0818-2232
---------
使用flask-sqlalchemy进行`SQLALCHEMY_DATABASE_URI`的设置使用sqlite还是要写技巧的
以下大段的都是 [http://docs.sqlalchemy.org/en/latest/core/engines.html](http://docs.sqlalchemy.org/en/latest/core/engines.html)上摘抄过来的，咱们只说这sqlite

#### SQLite

SQLite connects to file-based databases, using the Python built-in module sqlite3 by default.

As SQLite connects to local files, the URL format is slightly different. The “file” portion of the URL is the filename of the database. For a relative file path, this requires three slashes:

```
# sqlite://<nohostname>/<path>
# where <path> is relative:
engine = create_engine('sqlite:///foo.db')
```

And for an absolute file path, the three slashes are followed by the absolute path:

```
#Unix/Mac - 4 initial slashes in total
engine = create_engine('sqlite:////absolute/path/to/foo.db')
#Windows
engine = create_engine('sqlite:///C:\\path\\to\\foo.db')
#Windows alternative using raw string
engine = create_engine(r'sqlite:///C:\path\to\foo.db')
```

To use a SQLite :memory: database, specify an empty URL:

```
engine = create_engine('sqlite://')
```

More notes on connecting to SQLite at SQLite.
