from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy

# Create mongo_app
mongo_app = Flask('__name__')
mongo_app.config['MONGOALCHEMY_SERVER'] = 'ds055690.mongolab.com'
mongo_app.config['MONGOALCHEMY_SERVER_AUTH'] = False
mongo_app.config['MONGOALCHEMY_DATABASE'] = 'sidney'
mongo_app.config['MONGOALCHEMY_PORT'] = '55690'
mongo_app.config['MONGOALCHEMY_USER'] = "sid"
mongo_app.config['MONGOALCHEMY_PASSWORD'] = '123456'

# Create database connection object
mongo = MongoAlchemy(mongo_app)
