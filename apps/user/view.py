from flask import Blueprint, render_template, request, redirect, url_for, session, g
from werkzeug.security import generate_password_hash, check_password_hash

from apps import db
from apps.user.model import User

user_bp = Blueprint('user', __name__)  # 创建蓝图

# 使用白名单方式/黑名单方式
required_login_list = ['/base', '/loan/loan', '/loan/capital', '/loan/trend']


# 进入路由前执行 钩子函数
@user_bp.before_app_first_request
def first_request():
    print("before_app_first_request")


# 路由拦截
@user_bp.before_app_request
def before_request():
    print("before_app_request", request.path)
    if request.path in required_login_list:
        uid = session.get('uid')
        if uid:
            user = User.query.get(uid)
            g.user = user
        else:
            return redirect(url_for('user.login'))


# 路由结束 钩子 对response做特殊处理
@user_bp.after_app_request
def after_app_request(response):
    print("after_app_request")
    response.set_cookie("a", "bbb", max_age=1000)
    return response


# 路由结束 钩子 对response做特殊处理
@user_bp.teardown_app_request
def teardown_app_request(response):
    print("teardown_app_request")


@user_bp.route('/base', endpoint='base')
def base():
    user = g.user
    if user:
        return render_template('base.html', user=user)
    return render_template('base.html')


@user_bp.route('/login', endpoint='login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        uo = User.query.filter_by(username=username).first()
        if uo:
            if check_password_hash(uo.password, password):
                # cookie信息
                # response = redirect(url_for('loan.loan'))
                # response.set_cookie('uid', str(uo.id), max_age=1800)  # 设置cookie
                # return response
                # session使用 必须要配置秘钥： SECRET_KEY = "ABCDEFAD"
                session['uid'] = uo.id
                return redirect(url_for('loan.loan'))

        msg = "user not found or password is error"
        return render_template('user/login.html', msg=msg)
    return render_template('user/login.html')


@user_bp.route('/register', endpoint='register', methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        username = request.form.get('username')
        phone = request.form.get('phone')
        password = request.form.get('password')
        re_password = request.form.get('repassword')
        if password == re_password:
            user = User()
            user.username = username
            user.password = generate_password_hash(password)
            user.phone = phone
            db.session.add(user)  # 将user对象添加到session缓存
            db.session.commit()
            return redirect(url_for('user.login'))
    return render_template('user/register.html')


@user_bp.route('/logout', endpoint='logout', methods=['GET', 'POST'])
def user_logout():
    # response = redirect(url_for('user.base'))
    # response.delete_cookie('uid')
    # session删除
    # del session['uid']
    session.clear()
    return redirect(url_for('user.login'))

