from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

db_connect = sqlite3.connect('database.db')
print('Opened database successfully')

db_connect.execute('CREATE TABLE IF NOT EXISTS posts (title TEXT, post TEXT)')
print('Table created successfully')

db_connect.close()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/new')
def new_post():
    return render_template('new.html')

@app.route('/addrecord', methods = ['POST'])
def addrecord():
    db_connect = sqlite3.connect('database.db')
    cursor = db_connect.cursor()

    try:
        title = request.form['title']
        post = request.form['post']
        print(title)
        print(post)
        cursor.execute('INSERT INTO posts (title,post) VALUES (?,?)', (title, post))
        print("Executed!")
        db_connect.commit()
        message = 'Record succesfully added'
    except:
        db_connect.rollback()
        message = 'Error in insert operation'

    finally:
        return render_template('result.html', message = message)
        db_connect.close()
