from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from .config.config import config

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://mi:password@localhost:3306/whoscall"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


from app.model import Task
from app.controller import task


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    migrate.init_app(app, db)
    task.init_app(app)

    return app