from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy

# Create mongo_app
mongo_app = Flask('__name__')
mongo_app.config['MONGOALCHEMY_SERVER'] = 'ds027908.mongolab.com'
mongo_app.config['MONGOALCHEMY_SERVER_AUTH'] = False
mongo_app.config['MONGOALCHEMY_DATABASE'] = 'siberian'
mongo_app.config['MONGOALCHEMY_PORT'] = '27908'
mongo_app.config['MONGOALCHEMY_USER'] = "admin"
mongo_app.config['MONGOALCHEMY_PASSWORD'] = 'zarman12'

# Create database connection object
mongo = MongoAlchemy(mongo_app)
