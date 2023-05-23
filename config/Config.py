configs = dict()

email_config = {
    "MAIL_SERVER": 'smtp.163.com',
    "MAIL_PORT": 25,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": 'hyp19990919@163.com',
    "MAIL_PASSWORD": 'SHZROEMQFLKMQEEL',
    "MAIL_DUBUG": True,
    "MAIL_SALT": 'qsaFju!@#SDG1'
}

mysqldb_config = {
    'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://root:123456@127.0.0.1:3306/hfhs',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
}


def create_config() -> dict:
    configs.update(email_config)
    configs.update(mysqldb_config)
    return configs
