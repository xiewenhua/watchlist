from flask import Flask

app=Flask(__name__)

@app.route('/user/<name>')
def hello(name):
    return '<h1>Hello %s!</h1><img src="http://helloflask.com/totoro.gif">'%name