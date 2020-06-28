from datetime import datetime

from sqlalchemy.orm import backref

from apps.ext import db


# 用户表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(50))
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 建立表联系
    loans = db.relationship('Loan', backref='user')
    def __str__(self):
        return self.username


# 用户资产表
class UserFund(db.Model):
    __tablename__ = 'userfund'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    balance = db.Column(db.String(30))  # 可用余额
    pay_in_ing = db.Column(db.String(30))   # 待收入
    pay_out_ing = db.Column(db.String(30))  # 待支出
    update_time = db.Column(db.DateTime, default=datetime.now)


# 用户流水表
class UserBill(db.Model):
    __tablename__ = 'userbill'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    b_type = db.Column(db.String(1))
    fund_type = db.Column(db.String(1))
    number = db.Column(db.String(20))
    balance = db.Column(db.String(20))
    memo = db.Column(db.String(50))
    ref_info = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, default=datetime.now)


