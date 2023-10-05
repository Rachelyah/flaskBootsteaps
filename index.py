from flask import Flask, render_template
#兩個一樣的可以一起寫用逗號分開

app = Flask(__name__)

@app.route("/")
def index():
    names = ['喵喵', '咪咪', '饅頭', '郵局咪']
    return render_template('index.jinja.html', n = names)

@app.route("/feature")
def feature():
    return render_template('feature.jinja.html')

@app.route("/description")
def description():
    return render_template('description.jinja.html')

@app.route("/product")
def product():
    return render_template('product.jinja.html')