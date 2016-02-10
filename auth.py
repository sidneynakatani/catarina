from flask import Flask, request, jsonify, redirect, abort, json
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from db.connectionfactory import db
from model.credential import Credential
from model.key import Key
import hashlib, datetime

app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'home'



@app.route('/')
def home():
    return 'Hello!'


@app.route('/key/<passkey>', methods = ['GET'])
def getKey(passkey):
    key = Key.query.filter(Key.passKey == passkey).first()
    
    if key is None:
        abort(401)
        return 'Authorization denied'
    
    return jsonify(auth = True)



@app.route('/login', methods = ['POST','GET'])
def login():
    
    content_type = request.headers['Content-Type']
    method = request.method

    print content_type + ' : ' + method

    if method == 'POST':
	email = request.form.get('email','')
	password = request.form.get('password','')

    if method == 'GET':
        email = request.args.get('email')
        password = request.args.get('password')

    credential = Credential.query.filter_by(email = email, password = password).first()

    if credential is None:
        abort(401)
        return 'Authorization denied'

    hash = generateKey()
    login_user(credential)
    return jsonify(login = credential.active, key= hash)

@app.route('/signIn', methods = ['POST'])
def signIn():

    email = request.form.get('email','')
    password = request.form.get('password','')
    firstName = request.form.get('firstName','')
    lastName = request.form.get('lastName','')
    createdAt = datetime.datetime.now()
    credential = Credential(email, password, firstName, lastName, True, createdAt)
    db.session.add(credential)
    db.session.commit()
   
    return jsonify(created = True)

def generateKey():
    now = datetime.datetime.now()
    hash = hashlib.sha224(unicode(now)).hexdigest()
    key = Key(passKey = hash, createdAt = now)
    key.save();
    return hash

if __name__ == '__main__':
    app.run(debug=True)


