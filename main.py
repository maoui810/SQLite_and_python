import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

#cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
          #  (Title TEXT, Director TEXT, Year INT)''')

#cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver','Martin Scorsese',1976)")

#cursor.execute("SELECT * FROM Movies")

#famousFilms = [('Pulp Fiction', 'Quentin Tarantino', 1994),
             #  ('Back to the Future','Steven Steven', 1985),
              # ('Moonrise Kingdom','Wes Aderson',2012)]

#cursor.executemany('Insert INTO Movies VALUES (?,?,?)',famousFilms)
#records=cursor.execute("SELECT * FROM Movies")
#print(cursor.fetchall())


release_year = (1985,)

cursor.execute("SELECT * FROM Movies WHERE year=?",release_year)
print(cursor.fetchall())
connection.commit()
connection.close()
