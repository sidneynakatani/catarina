from db.connectionfactory import db
from db.mongodbfactory import mongo
from model.credential import Credential
from model.post import Author 
from model.key import Key
import datetime
#Test Postgree

#db.drop_all(bind=None)
#db.create_all()

#credential = Credential('admin@example.com', '123456', 'a', 'b', True)
#db.session.add(credential)
#db.session.commit()


#a = Credential.query.filter_by(first_name='a', last_name='b').first()
#print a.last_name
#print a.active


#Test Mongodb

#key = Key(passKey='abcdef', createdAt=datetime.datetime.now())
#key.save();

#key = Key.query.filter(Key.passKey == 'abcdef').first()
#print key.createdAt


