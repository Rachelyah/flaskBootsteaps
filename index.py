from flask import Flask, render_template
#兩個一樣的可以一起寫用逗號分開

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.jinja.html')

@app.route("/feature")
def feature():
    return render_template('feature.jinja.html')