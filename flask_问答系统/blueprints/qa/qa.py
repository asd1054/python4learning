from flask import Blueprint, render_template

bp = Blueprint('user', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/login')
def login():
    return '欢迎登录'
