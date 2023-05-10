import flask

app = flask.Flask(__name__)

@app.route('/home')
def home():
    return 'Hello, World!'

@app.route('/exit')
def exit():
    return 'Goodbye!'
    
@app.route('/gratitude')
def gratitude():
    return "Gratidão \o/"

@app.route("/", methods=["GET", "POST"])
def response():
    if flask.request.method == "POST":
        return "POST method called"
    return "GET method called"