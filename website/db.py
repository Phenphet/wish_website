import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('''
             CREATE TABLE Liquor_anniversary_TB (
             Id INTEGER PRIMARY KEY AUTOINCREMENT ,
             Detail TEXT, 
             Full_name TEXT, 
             Position TEXT,
             Agency TEXT
             )''')

print("Created table successfully!")

conn.close()