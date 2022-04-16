HOSTNAME = '172.22.187.253'  # 使用的是zetorir的内网ip
PORT = '3306'
DATABASE = 'wk_flask'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'

