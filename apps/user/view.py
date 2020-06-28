from flask import Blueprint, render_template, request, redirect, url_for

from apps import db
from apps.user.model import User

user_bp = Blueprint('user', __name__)  # 创建蓝图


@user_bp.route('/')
def base():
    return render_template('base.html')


@user_bp.route('/login', endpoint='login')
def user_login():
    return render_template('user/login.html')


@user_bp.route('/register', endpoint='register')
def user_register():
    return render_template('user/register.html')