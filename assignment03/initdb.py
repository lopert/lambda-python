import sqlite3

connection = sqlite3.connect('database.db')
print ('Opened database successfully')

connection.execute('CREATE TABLE IF NOT EXISTS foods (name TEXT, calories TEXT, cuisine TEXT, is_vegetarian TEXT, is_gluten_free TEXT)')
print ('Table created successfully')

connection.execute('INSERT INTO foods (name, calories, cuisine, is_vegetarian, is_gluten_free) VALUES (?,?,?,?,?)', ("shwarma", "9001", "Middle Eastern", "false", "no"))
print ('Shwarma inserted')
connection.commit()

connection.close()
