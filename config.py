
class Config:
    """Base config."""
    SECRET_KEY = " asecretisasecret "


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True


class TestConfig(Config):
    FLASK_ENV = 'testing'
    DEBUG = False
    TESTING = True
