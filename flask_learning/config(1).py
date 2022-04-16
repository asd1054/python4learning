HOSTNAME = '172.22.187.253'  # 使用的是zetorir的内网ip
PORT = '3306'
DATABASE = 'wk_flask'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'


class Config:
    # from_object 只能识别模块，类，字符串，不能识别字典
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JSON_AS_ASCII = False
