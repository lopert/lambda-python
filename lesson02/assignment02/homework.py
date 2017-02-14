from flask import Flask, render_template, jsonify

app = Flask(__name__)

#basis
@app.route('/')
def index():
    return 'Hello World'

@app.route('/birthday')
def birthday():
    return 'March 23 1989'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' + name + "!"

#this one is supposed to override just '/' but yolo
@app.route('/home')
def home():
    return render_template('home.html')

#extra credit
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1 + num2)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    return str(num1 * num2)

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    return str(num1 - num2)

@app.route('/favoritefoods')
def favouritefoods():
    favs = ['pizza','panini','smoothie']
    return jsonify(favs)
