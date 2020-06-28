from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps import create_app
from apps.ext import db
from apps.user.model import *
from apps.loan.model import *

app = create_app()  # 创建flask app
manager = Manager(app=app)  # 命令管理app

# 配置 migrate 数据库命令管理工具关联  既影响app  又能让manager进行命令管理
migrate = Migrate(app=app, db=db)  # 关联app  操作数据库
manager.add_command('db', MigrateCommand)  # 命令交给manager管理


@manager.command
def init():   # 自定义启动命令
    print('manager defined app init command')


if __name__ == '__main__':
    manager.run()