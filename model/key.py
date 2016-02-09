from db.mongodbfactory import mongo


class Key(mongo.Document):
    passKey = mongo.StringField()
    createdAt = mongo.DateTimeField()

