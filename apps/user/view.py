from flask import Blueprint, render_template, request, redirect, url_for

from apps import db
from apps.user.model import User

user_bp = Blueprint('user', __name__)  # 创建蓝图


@user_bp.route('/')
def user_login():
    users = User.query.all()
    return render_template('user/login.html', users=users)
