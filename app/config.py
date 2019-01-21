import os
import app


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'thisismyireportersecretkey'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True

app_config={
    'development':DevelopmentConfig,
    'testing': TestingConfig
}
