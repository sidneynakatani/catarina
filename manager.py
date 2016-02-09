from db.connectionfactory import db
from db.mongodbfactory import mongo
from model.credential import Credential
from model.post import Author 

#Test Postgree

#db.drop_all(bind=None)
#db.create_all()

#credential = Credential('admin@example.com', '123456', 'a', 'b', True)
#db.session.add(credential)
#db.session.commit()


a = Credential.query.filter_by(first_name='a', last_name='b').first()
print a.last_name
print a.active


#Test Mongodb

#mark_pilgrim = Author(name='Mark')
#mark_pilgrim.save()
#mark = Author.query.filter(Author.name == 'Mark Pilgrim').first()
#print mark.name

