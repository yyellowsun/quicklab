class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://hky:hky2000328@127.0.0.1:3306/lab'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # used for encryption and session management
    SECRET_KEY = 'mysecretkey'