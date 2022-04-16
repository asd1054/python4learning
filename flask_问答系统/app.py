from flask import Flask, request, render_template
from config import Config
from exts import db
from blueprints import qa_bp
from blueprints import user_bp

# 使用一个Flask创建一个app对象，并且传递__name__参数
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)  # db = SQLAlchemy(app)


# 加个name 就能注册多个蓝图，原来那么简单额
app.register_blueprint(qa_bp, name="qa_bp", url_prefix='/')
app.register_blueprint(user_bp, name="user_bp", url_prefix='/user')

if __name__ == "__main__":

    app.run(debug=True)
