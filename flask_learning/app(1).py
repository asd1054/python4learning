from flask import Flask, request, render_template
from config import Config
from flask_migrate import Migrate
from models import User, UserExtension, Article, LoginForm
from exts import db

# 使用一个Flask创建一个app对象，并且传递__name__参数
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)  # db = SQLAlchemy(app)

migrate = Migrate()
migrate.init_app(app=app, db=db)  # migrate = Migrate(app,db)

# 必须是app.py 或者wsgi.py
# flask db init

# flask db migrate -m 'first init db'

# flask db upgrade


# db.drop_all()
# db.create_all()
# 有隐患，并不利于后期增加，只适合开始的时候初始化使用

# @app.route("/createall")
# def create_all():
#     db.create_all()
#     return "create_all"


# @app.route("/dropall")
# def create_all():
#     db.drop_all(app=app)
#     return "drop_all"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            return '登录成功'
        else:
            return "邮箱或密码错误"


@app.route("/oto")
def ont_to_one():
    user = User(username="wukong")
    extension = UserExtension(school='清华大学')
    user.extension = extension
    db.session.add(user)
    db.session.commit()
    return "ont_to_one"


@app.route("/otm")
def one_to_many():
    article1 = Article(title='第一篇文章', content='xxxx')
    article2 = Article(title='第2篇文章', content='yyyyy')
    user = User(username='wukong')
    article1.author = user
    article2.author = user
    db.session.add(article1, article2)
    db.session.commit()
    return "one to many 数据库操作成功"


@app.route('/article')
def article_view():
    # 1.添加数据
    # article = Article(title='这是第一篇文章', content='内容怎么写呢')
    # db.session.add(article)
    # # 做一个提交操作
    # db.session.commit()

    # 2.查询数据
    # article = Article.query.filter_by(id=1)  # 返回一个类列表的对象
    # print(article)
    # print(article[0])
    # print(article[0].title)

    # 3.修改数据
    # article = Article.query.filter_by(id=1)[0]
    # article.content = 'yyyyyyyyyyyy'
    # db.session.commit()

    # 4.删除数据
    # Article.query.filter_by(id=1).delete()
    # db.session.commit()
    return "数据提交成功"


@app.route("/")
def hello():
    engine = db.get_engine()
    with engine.connect() as conn:
        result = conn.execute("select 1").fetchone()
        print(result)
    return 'hello worldssssss!' + str(result) + '这是一个结尾'


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080, debug=True)
