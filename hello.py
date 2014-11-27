from flask import Flask,json,request
from db.connectionfactory import ConnectionFactory
from db.connectionfactory import db
from model.user import User
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/test')
def test():
    conn = ConnectionFactory()
    return conn.create()

@app.route('/<name>')
def hello_name(name):
    user = User.query.filter_by(first_name=name).first()
    return jsonify(first_name = user.first_name, last_name = user.last_name, active = user.active)

@app.route('/messages', methods = ['POST'])
def api_message():
    return json.dumps(request.json)

if __name__ == '__main__':
    app.run(debug=True)


