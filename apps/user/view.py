from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from apps import db
from apps.user.model import User

user_bp = Blueprint('user', __name__)  # 创建蓝图


@user_bp.route('/')
def base():
    return render_template('base.html')


@user_bp.route('/login', endpoint='login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        uo = User.query.filter_by(username=username).first()
        if uo:
            if check_password_hash(uo.password, password):
                return redirect(url_for('loan.loan'))
        msg = "user not found or password is error"
        return render_template('user/login.html', msg=msg)
    return render_template('user/login.html')


@user_bp.route('/register', endpoint='register', methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        print(1)
        username = request.form.get('username')
        phone = request.form.get('phone')
        password = request.form.get('password')
        print(password)
        re_password = request.form.get('repassword')
        print(re_password)
        if password == re_password:
            print(2)
            user = User()
            user.username = username
            user.password = generate_password_hash(password)
            user.phone = phone
            print(user)
            db.session.add(user)  # 将user对象添加到session缓存
            db.session.commit()
            return redirect(url_for('user.login'))
    return render_template('user/register.html')
