class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/test'  # 连接数据库。示例：mysql://username:password@host/post/db?charset=utf-8
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它
    SQLALCHEMY_ECHO = True  # 调试设置为true


class DeploymentConfig(Config):
    DEBUG = True
    ENV = 'deployment'


class DeploymentConfigHome(Config):
    DEBUG = True
    ENV = 'deployment'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:19861111@127.0.0.1:3306/test'  # 连接数据库。示例：mysql://username:password@host/post/db?charset=utf-8


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
