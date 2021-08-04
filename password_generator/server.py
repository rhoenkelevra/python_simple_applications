from flask import Flask, render_template

# create flask instance
app = Flask(__name__)


@app.route('/')
def index():
    '''create a route decorator'''
    return render_template("index.html")


@app.route('/user/<name>')
def user(name):
    '''localhost:5000/user/<name>'''
    return "<h1>Hello {}</h1>".format(name)
