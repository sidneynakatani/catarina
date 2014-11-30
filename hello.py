from flask import Flask, request, jsonify, redirect
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from db.connectionfactory import ConnectionFactory
from model.user import User
from model.post import Author

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



@app.route('/<name>')
@login_required
def hello_name(name):
    author = Author.query.filter(Author.name == name).first()
    return redirect(jsonify(name = author.name))



@app.route('/auth', methods = ['POST','GET'])
def auth():
    
    if request.method == 'POST':
    	#email = request.form['email'] 
    	#password =  request.form['password']
    	email = request.form.get('email','')
	password = request.form.get('password','')
	print 'POST Method' + email + ' : ' + password

    if request.method == 'GET':
        email = request.args.get('email')
        password = request.args.get('password')
    	print 'GET Method'

    user = User.query.filter_by(email = email, password = password).first()

    if user is None:
        return 'Authorization denied'

    login_user(user)
    return jsonify(auth = user.active)




@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))



if __name__ == '__main__':
    app.run(debug=True)


