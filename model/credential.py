from db.connectionfactory import db

class Credential(db.Model):

    __tablename__ = 'credential'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(30))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    active = db.Column(db.Boolean())
    update_date = db.Column(db.DateTime())

    def __init__(self, email, password, first_name, last_name, active, update_date):

        self.email = email
        self.password = password
        self.first_name = first_name
	self.last_name = last_name
        self.active = active
        self.update_date = update_date

    
    def is_authenticated(self):
        return True

 
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


    def __repr__(self):
        return '<Credential %r>' % (self.first_name)
