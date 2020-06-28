from flask import Blueprint, render_template, request, redirect, url_for


loan_bp = Blueprint('loan', __name__, url_prefix='/loan')  # 创建蓝图


@loan_bp.route('/loan', endpoint='loan')
def loan_show():
    return render_template('loan/loan.html')


@loan_bp.route('/capital', endpoint='capital')
def loan_capital():
    return render_template('loan/capital.html')


@loan_bp.route('/trend', endpoint='trend')
def loan_trend():
    return render_template('loan/trend.html')
