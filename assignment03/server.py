from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

#base
@app.route('/')
def main():
    return render_template('home.html')

@app.route('/enternew')
def enternew():
    return render_template('food.html')

@app.route('/addfood', methods = ['POST'])
def addfood():
    db_connect = sqlite3.connect('database.db')
    cursor = db_connect.cursor()

    try:
        name = request.form['name']
        calories = request.form['calories']
        cuisine = request.form['cuisine']
        is_vegetarian = request.form['is_vegetarian']
        is_gluten_free = request.form['is_gluten_free']

        #(name TEXT, calories TEXT, cuisine TEXT, is_vegetarian TEXT, is_gluten_free TEXT)
        cursor.execute('INSERT INTO foods (name, calories, cuisine, is_vegetarian, is_gluten_free) VALUES (?,?,?,?,?)', (name, calories, cuisine, is_vegetarian, is_gluten_free))
        print("Executed!")
        db_connect.commit()
        message = 'Record succesfully added'
    except:
        db_connect.rollback()
        message = 'Error in insert operation'

    finally:
        return render_template('result.html', message = message)
        db_connect.close()

#extra credit
import json

@app.route('/favorite')
def favorite():
    db_connect = sqlite3.connect('database.db')
    cursor = db_connect.cursor()

    try:
        cursor.execute('SELECT * FROM foods WHERE name = "shwarma"')
        message = json.dumps(cursor.fetchall())
    except:
        db_connect.rollback()
        message = 'Error in fav operation'
    finally:
        return render_template('result.html', message = message)
        db_connect.close()

@app.route('/search', methods = ['GET'])
def search():
    db_connect = sqlite3.connect('database.db')
    cursor = db_connect.cursor()

    try:
        search_string = request.args.get('name')
        query = 'SELECT * FROM foods WHERE name = \"' + search_string + '\"'
        cursor.execute(query)
        message = json.dumps(cursor.fetchall())
    except:
        db_connect.rollback()
        message = 'Error in search operation'
    finally:
        return render_template('result.html', message = message)
        db_connect.close()

@app.route('/drop')
def drop():
    db_connect = sqlite3.connect('database.db')
    cursor = db_connect.cursor()

    try:
        query = 'DROP TABLE foods'
        cursor.execute(query)
        message = 'Dropped'
    except:
        db_connect.rollback()
        message = 'Error in drop operation'
    finally:
        return render_template('result.html', message = message)
        db_connect.close()
