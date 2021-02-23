from flask import Flask
app=Flask(__name__)

@app.route('/')
def Home():
    return "<h1>Hello World</h1>"

@app.route('/John')
def John():
    return "<h1>Hello John</h1>"

@app.route("/")
def Hello():
    return 'Open a new tab and enter /Welcome/name for URL'

@app.route('/Welcome/<name>')
def Welcome_name(name):
    return 'Welcome ' + name +'!'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)               