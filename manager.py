from db.connectionfactory import db
from model.user import User

db.drop_all(bind=None)
db.create_all()

user = User('admin@example.com', '123456', 'a', 'b', True)
db.session.add(user)
db.session.commit()


a = User.query.filter_by(first_name='a').first()
print a.last_name
print a.active

