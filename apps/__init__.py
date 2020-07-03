from flask import Flask
import settings
from apps.ext import db
from apps.user.view import user_bp
from apps.loan.view import loan_bp
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.DeploymentConfigHome)  # 加载settings配置
    app.register_blueprint(user_bp)  # 将蓝图对象user_bp 绑定到app上 print(app.url_map)
    app.register_blueprint(loan_bp)  # 将蓝图对象user_bp 绑定到app上 print(app.url_map)
    db.init_app(app)  # 将db对象与app进行关联
    bootstrap.init_app(app)  # app挂载bootstrap
    # print(app.url_map)  # 打印蓝图
    return app
