from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/messages', methods = ['POST'])
def api_message():
    return "JSON Message: " + json.dumps(request.json)

if __name__ == '__main__':
    app.run(debug=True)


