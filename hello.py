from flask import Flask, request, jsonify, redirect, abort, json
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from db.connectionfactory import ConnectionFactory
from model.user import User
from model.post import Author
from model.pet import Pet

app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'home'



@app.route('/')
def home():
    return 'Hello!'



@app.route('/test')
@login_required
def test():
    conn = ConnectionFactory()
    return conn.create()



@app.route('/pet/get/<userId>', methods = ['GET'])
@login_required
def getPet(userId):
    pet = Pet.query.filter(Pet.userId == userId).first()
    return jsonify(pet_name = pet.petName, pet_img = pet.petImg, pet_location = pet.petLocation, description = pet.description)



@app.route('/pet/add', methods = ['POST'])
@login_required
def addPet():
    userId = request.json.get('userId')
    petName = request.json.get('petName')
    petImg = request.json.get('petImg')
    petLocation = request.json.get('petLocation')
    description = request.json.get('description')
    pet = Pet(userId=userId, petName=petName, petImg=petImg, petLocation=petLocation, description=description)
    pet.save()
    return 'OK'


@app.route('/login', methods = ['POST','GET'])
def login():

    """  Post method:
         Content-Type: application/x-www-form-urlencoded 
    """
    
    content_type = request.headers['Content-Type']
    method = request.method

    #print content_type + ' : ' + method

    if method == 'POST':
	email = request.form.get('email','')
	password = request.form.get('password','')

    if method == 'GET':
        email = request.args.get('email')
        password = request.args.get('password')

    user = User.query.filter_by(email = email, password = password).first()

    if user is None:
        abort(401)
        return 'Authorization denied'

    login_user(user)
    return jsonify(login = user.active)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")



@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


if __name__ == '__main__':
    app.run(debug=True)


