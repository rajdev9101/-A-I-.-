from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "yes i am Raj how can i help you !"
