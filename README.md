# flask-admin
Win虚拟环境搭建：

1. 安装虚拟环境管理包  CMD:  pip install virtualenv
2. 创建虚拟环境   CMD: virtualenv 环境名称
3. 激活虚拟环境   cd  path/环境路径/Scripts   CMD:activate
4. 退出虚拟环境  deactivate

管理虚拟环境工具： virtualenvwrapper

pip install virtualenvwrapper-win

1. 创建环境： mkvirtualenv 环境名   默认创建路径为c:\user\envs   变更路径需创建新环境变量：WORKON_HOM  配置指定路径 重启生效
2. 指定版本python  mkvirtualenv --python==python路径/python2.X.exe  环境名
3. 进入环境  workon 环境名
4. 删除虚拟环境  rmvirtualenv 环境名
5. 列出所有虚拟环境 lsvirtualenv
6. 进入虚拟环境目录： cdvirtualenv 环境名



过滤器：

flask

request  [object]

【get】request.args.get('name')

【post】requset.form.get('name')

response [object]

redirect(url_for('index',name=name))

app.config()



jijan2 -- 

条件

{% if loop.first %}

{% elif %}

{% endif %}

循环

{% for i in object %}

{{ loop.index }}

{% endfor %}

过滤器

{{ name | length }}

{{ name | first }}

自定义过滤器：

通过flask-object:

1.add_template_filter(name)

2.使用装饰器完成 @app.template.filter(name)

template复用

{% block middle%} {% endblock%}

include  引用公共模块

{% include ‘common/xxx.html’ %}

宏 macro

1.jinja2 的一个函数   返回一个HTML字符串

2.代码复用 避免代码冗余

定义：{% macro form(action, value='Form Submit', method='post') %} {% endmacro %}

导入：{% import 'macro/macro.html' as f %}

调用：{{ f.form('/') }}

set全局变量 with局部变量的使用

{% set name="hello" %}

{{ name }}

{% whth num=100 %}

{{ num }} 

{% endwith %}



模型及相关插件扩展：

pip install flask-script    命令管理工具

manager   自带命令：shell  runserver --help

pip install pymysql   数据连接驱动

pip install flask-sqlalchemy      ORM映射管理工具

pip install flask-migrate   命令发布工具

-- 环境搭建

1. 配置：settings 

   ```python
   SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123465@127.0.0.1:3306/flask'
   ```

2. 关联: 创建ext包

   __init__.py   db=SQLAlchemy()

   ```python
   def create_app():
   	db.init_app(app)  # 将db对象与app进行关联
   ```

3. 关联migrate

   ```python
   migrate = Migrate(app=app, db=db)  # 关联app  操作数据库
   manager.add_command('db', MigrateCommand)  # 命令交给manager管理
   ```

python app.py db --help 查看migrate的相关命令

命令使用：

初始化：

1.app.py 中导入模型

```
from apps.user.model import User
```

2.初始化

python app.py db init

3.python app.py db migrate   迁移 生成版本文件

生成versions文件  migrations/versions/bcf23432.py

4.upgrade 执行创建表命令

.python app.py db upgrade  同步

python app.py db downgrade 版本号       -- 选择版本号

回话机制

A.cookie
设置：
resoponse = redirect(url_for('XXX.XXX'))
resoponse.set_cookie(key,value,max_age=1000)
获取:
request.cookies.get(key)---->value
删除:
1.创建response对象
response = redirect(url_for('XXX.XXX'))
response = render_template(url_for('XXX.XXX'))
response = Response()
response = make_response()
response = jsonify()
2.通过对象调用删除方法
response.delete_cookie(key)

B.session
cookie方式存在客户端不安全，使用session把信息存在服务端更为安全
1.session对象创建
引入session
from flask import session
session[key]=value
2.获取
uid = session['uid']
3.删除
del session['uid']
session.clear()
