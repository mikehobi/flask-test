import os


# default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '\xf1\x92<~\x92\xdbW\x9b\xe4\xd95\x90B\xbf\xd8\rC6\xa9\xca\x87M\xe1\x85'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SLACK_TOKEN = os.environ['SLACK_TOKEN']
	WEBHOOK = os.environ['WEBHOOK']
	TEAM_ID = os.environ['TEAM_ID']


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False