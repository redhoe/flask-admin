from flask import Blueprint, render_template, request, redirect, url_for


loan_bp = Blueprint('loan', __name__, url_prefix='/loan')  # 创建蓝图


@loan_bp.route('/show', endpoint='show')
def loan_show():
    return render_template('base.html')
