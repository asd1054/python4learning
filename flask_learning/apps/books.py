from flask import Blueprint, render_template, request

bp = Blueprint(
    'books', __name__, url_prefix='/books', template_folder='../templates/books'
)  # ,


@bp.route('/')
def index():
    return "欢迎来到图书馆"


@bp.route('/<username>')
def get_username(username):
    # username = request.args.get('username')
    context = {"username": ''}
    if username:
        context = {"username": username}

    return render_template('test.html', **context)
