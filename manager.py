from db.connectionfactory import db
from db.mongodbfactory import mongo
from model.user import User
from model.post import Author 

#db.drop_all(bind=None)
#db.create_all()

#user = User('admin@example.com', '123456', 'a', 'b', True)
#db.session.add(user)
#db.session.commit()


a = User.query.filter_by(first_name='a').first()
print a.last_name
print a.active

#mark_pilgrim = Author(name='Mark Pilgrim')
#mark_pilgrim.save()
mark = Author.query.filter(Author.name == 'Mark Pilgrim').first()
print mark.name

