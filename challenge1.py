import sqlite3

connection = sqlite3.connect('users.db')

cursor = connection.cursor()

#cursor.execute('''CREATE TABLE IF NOT EXISTS Users
               # (User_ID INT,First_Name TEXT NOT NULL,
               # Last_Name TEXT NOT NULL,Email TEXT NOT NULL UNIQUE)''')

# cursor.execute("INSERT INTO Users VALUES (2,'JO','Singh','JO@gmail.com')")

cursor.execute("SELECT * FROM Users")

people = [(3, 'MO', 'Singh', 'JMO@gmail.com'),
          (4, 'JJ', 'Singh', 'JJ@gmail.com'),
          (5, 'MOOC', 'Singh', 'moco@gmail.com'),
          (2, 'JO', 'Singh', 'JO@gmail.com'),
          (1, 'dd', 'Singh', 'MO@gmail.com')]

cursor.executemany('Insert INTO Users VALUES (?,?,?,?)', people)
records = cursor.execute("SELECT Email FROM Users ")
print(cursor.fetchall())

