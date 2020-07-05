import time

from flask import Blueprint, render_template, request, redirect, url_for, g

from apps import db
from apps.loan.model import Trend, Loan, Capital
from apps.user.model import User

loan_bp = Blueprint('loan', __name__, url_prefix='/loan')  # 创建蓝图


@loan_bp.route('/loan', endpoint='loan', methods=['GET', 'POST'])
def loan_show():
    user = g.user

    if request.method == 'POST':
        bankname = request.form.get('bankname')
        loanname = request.form.get('loanname')
        amount = request.form.get('amount')
        amountrates = request.form.get('amountrates')
        rate = request.form.get('rate')
        begintime = request.form.get('begintime')
        endtime = request.form.get('endtime')

        if bankname and loanname and amount and amountrates and rate and endtime and begintime:
            loan = Loan()
            loan.user_id = user.id
            loan.bank_name = bankname
            loan.loan_name = loanname
            loan.amount = amount
            loan.balance = amount
            loan.amount_rates = amountrates
            loan.balance_rates = amountrates
            loan.rate = rate
            loan.begin_time = begintime
            loan.end_time = endtime
            db.session.add(loan)  # 将user对象添加到session缓存
            db.session.commit()
    loans = Loan.query.filter_by(user_id=g.user.id).all()
    return render_template('loan/loan.html', user=g.user, loans=loans)


@loan_bp.route('/capital', endpoint='capital', methods=['GET', 'POST'])
def loan_capital():
    user = g.user
    loans = Loan.query.filter_by(user_id=g.user.id).order_by(Loan.id.desc()).all()

    if request.method == 'POST':
        loan_id = request.form.get('loan_id')
        amount = request.form.get('amount') # 总金额
        balance = request.form.get('balance')  # 本金 ‘0’: -  ‘1’：+
        rate = request.form.get('rate')  # 利息 ‘0’: -  ‘1’：+
        side = request.form.get('side')  # 方向 ‘0’: -  ‘1’：+
        status = request.form.get('status')  # ‘0’：待执行   ‘1’：已执行
        expect_time = request.form.get('expect_time')  # 预计执行时间
        execute_time = request.form.get('execute_time')  # 实际执行时间
        if loan_id and amount and balance and rate and side and status and expect_time and execute_time:
            capital = Capital()
            capital.loan_id = loan_id
            capital.amount = amount
            capital.side = side
            capital.status = status
            capital.balance = balance
            capital.rate = rate
            capital.user_id = user.id
            capital.expect_time = expect_time
            capital.execute_time = execute_time
            db.session.add(capital)
            # db.session.commit()
            if status == '2':
                loan_obj = Loan.query.filter(Loan.id == loan_id).first()
                loan_obj.balance = str(float('%.2f' % float(loan_obj.balance)) - float('%.2f' % float(balance)))
                loan_obj.balance_rates = str(float('%.2f' % float(loan_obj.balance_rates)) - float('%.2f' % float(rate)))

            db.session.commit()
    capitals = Capital.query.filter_by(user_id=g.user.id).order_by(Capital.id.desc()).all()
    response = render_template('loan/capital.html', user=user, loans=loans, capitals=capitals)
    return response


@loan_bp.route('/trend', endpoint='trend')
def loan_trend():
    loan_name = "地狱贷"
    trends = Trend.query.filter_by(loan_name=loan_name)
    return render_template('loan/trend.html', trends=trends, user=g.user)


# 返回"loan_name"的折线数据
@loan_bp.route('/get_trend', endpoint='get_trend')
def get_trend():
    loan_name = "地狱贷"
    trends = Trend.query.filter_by(loan_name=loan_name)
    redict = dict()
    redict['loan_name'] = loan_name
    balance_list = list()
    balance_rates_list = list()
    date_list = list()
    for t in trends:
        balance_list.append(t.balance)
        balance_rates_list.append(t.balance_rates)
        date_list.append(t.month)
    redict['balance_list'] = balance_list
    redict['balance_rates_list'] = balance_rates_list
    redict['date_list'] = date_list
    time.sleep(0.1)
    return redict

