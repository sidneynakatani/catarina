from flask import Flask,json,request
from db.connectionfactory import ConnectionFactory

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/test')
def test():
    return ConnectionFactory.create()

@app.route('/messages', methods = ['POST'])
def api_message():
    return json.dumps(request.json)

if __name__ == '__main__':
    app.run(debug=True)


