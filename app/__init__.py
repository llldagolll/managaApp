from flask import Flask
from app.lib.db import init_db
from app.views import index
import logging.handlers

def create_app(config_file):

    logging.info('start create app')

    app = Flask(__name__)
    app.config.from_object(config_file)

    #log output
    #fh = logging.FileHandler(app.config['LOGFILE'])
    fh = logging.handlers.RotatingFileHandler(app.config['LOGFILE'], maxBytes=1000000000, backupCount=30)
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    app.logger.addHandler(fh)

   # init_mail(app)
    init_db(app)

    #add views
    app.register_blueprint(index.app)


    return app
