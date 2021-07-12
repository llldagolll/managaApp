import os
import socket

base_dir = os.path.dirname(os.path.realpath(__file__))

class BaseConfig(object):
    ENV = None
    Testing = False


class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:nbroot@localhost/memo?charset=utf8'
    #app.config['SQLALCHEMY_DATABASE_URI']
    host = socket.gethostname()
    localhost = socket.gethostbyname(host)
    ENV = 'development'
   # SERVER_IP=localhost
    SERVER_IP='127.0.0.1'
    SERVER_PORT=8000
    LOGFILE = 'log/development.log'
    DEBUG = True
