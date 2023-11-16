from flask import Flask  # Import głównej klasy Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/info")  # Odnośnik URL  (ogólnie jest to dekorator)
def info():
    return "Hello World! :)"


