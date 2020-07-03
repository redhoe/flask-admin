import time

from flask import Blueprint, render_template, request, redirect, url_for, g

from apps.loan.model import Trend
from apps.user.model import User

loan_bp = Blueprint('loan', __name__, url_prefix='/loan')  # 创建蓝图


@loan_bp.route('/loan', endpoint='loan', methods=['GET', 'POST'])
def loan_show():
    if request.method == 'POST':
        username = request.form.get('username')
        phone = request.form.get('phone')
        password = request.form.get('password')
        re_password = request.form.get('repassword')
    return render_template('loan/loan.html', user=g.user)


@loan_bp.route('/capital', endpoint='capital', methods=['GET', 'POST'])
def loan_capital():
    if request.method == 'POST':
        username = request.form.get('username')
        phone = request.form.get('phone')
        password = request.form.get('password')
        re_password = request.form.get('repassword')
    return render_template('loan/capital.html', user=g.user)


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
