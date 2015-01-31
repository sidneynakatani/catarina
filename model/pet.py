from db.mongodbfactory import mongo


class Pet(mongo.Document):
    userId = mongo.StringField()
    petName = mongo.StringField()
    petImg = mongo.StringField()
    petLocation = mongo.StringField()
    description = mongo.StringField()
