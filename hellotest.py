from flask import Flask, render_template
app = Flask(__name__)


@app.route('/John')
def John():
    return "<h1>Hello John</h1>"

@app.route('/Welcome/<name>')
def Welcome_name(name):
    return 'Welcome ' + name +'!'

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True)               