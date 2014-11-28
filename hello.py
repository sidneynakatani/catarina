from flask import Flask,request,jsonify
from db.connectionfactory import ConnectionFactory
from model.user import User
from model.post import Author

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/test')
def test():
    conn = ConnectionFactory()
    return conn.create()

@app.route('/<name>')
def hello_name(name):
    author = Author.query.filter(Author.name == name).first()
    return jsonify(name = author.name)

@app.route('/auth', methods = ['POST'])
def auth():
    email = request.form['email'] 
    password =  request.form['password']
    user = User.query.filter_by(email = email, password = password).first()
    return jsonify(auth = user.active)


if __name__ == '__main__':
    app.run(debug=True)


