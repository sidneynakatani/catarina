from db.mongodbfactory import mongo


class Author(mongo.Document):
    name = mongo.StringField()
