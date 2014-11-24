from flask import Flask,json,request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/messages', methods = ['POST'])
def api_message():
    return json.dumps(request.json)

if __name__ == '__main__':
    app.run(debug=True)


