class Config(object):
	DEBUG = False
	TESTING = True

	db_username = 'baa07011a9ae85'
	db_password = '0d6b9c80'
	db_host = 'us-cdbr-east-04.cleardb.com'
	db_db = 'heroku_28f4d0761a66b96'

	SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(db_username, ,db_password, db_host, db_db)

class ProductionConfig(object):
	pass

class DevelopmentConfig(object):
	DEBUG = True