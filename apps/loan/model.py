from datetime import datetime

from sqlalchemy.orm import backref

from apps import db


# 银行记录表
class Loan(db.Model):
    __tablename__ = 'loan'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bank_name = db.Column(db.String(50), nullable=False)  # 银行名称
    loan_name = db.Column(db.String(50))  # 贷款名称
    amount = db.Column(db.String(30), default='0')   # 总金额
    balance = db.Column(db.String(30), default='0')  # 本金余额
    amount_rates = db.Column(db.String(30), default='0')  # 总利息
    balance_rates = db.Column(db.String(30), default='0')  # 利息余额
    rate = db.Column(db.String(30), default='0')  # 利率
    begin_time = db.Column(db.String(50))  # 开始时间
    end_time = db.Column(db.String(50))  # 结束时间
    create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间

    # 建立表联系
    capitals = db.relationship('Capital', backref='loan')

    def __str__(self):
        return self.loan_name


# 操作流水表
class Capital(db.Model):
    __tablename__ = 'capital'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    loan_id = db.Column(db.Integer, db.ForeignKey('loan.id'), nullable=False)
    amount = db.Column(db.String(30))  # 金额
    side = db.Column(db.String(1))  # 方向 ‘0’: -  ‘1’：+
    status = db.Column(db.String(1))  # ‘0’：待执行   ‘1’：已执行
    expect_time = db.Column(db.String(50))  # 预计执行时间
    execute_time = db.Column(db.String(50))  # 实际执行时间
    create_time = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.__tablename__


# 图表数据
class Trend(db.Model):
    __tablename__ = 'trend'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    loan_name = db.Column(db.String(30))  # comment='款项名'
    amount = db.Column(db.String(30))  # , comment='总金额'
    balance = db.Column(db.String(30))  # 剩余金额
    less_amount = db.Column(db.String(30))  # 还款金额
    amount_rates = db.Column(db.String(30))  # 总利息
    less_rates = db.Column(db.String(30), comment='还款利息')  # 还款利息
    balance_rates = db.Column(db.String(30))  # 利息余额
    month = db.Column(db.String(50))  # 实际执行时间
    create_time = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.__tablename__

