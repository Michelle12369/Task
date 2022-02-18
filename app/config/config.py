import os

basedir = os.path.abspath(os.path.dirname(__file__))


def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(basedir, db_name)

class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ContainerConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mi:password@host.docker.internal:3306/whoscall'

class DevelopmentConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mi:password@localhost:3306/whoscall'

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri("test.db")


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'container': ContainerConfig
}