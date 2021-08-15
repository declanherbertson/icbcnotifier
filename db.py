import sqlite3 as sl

def setup():
  con = sl.connect('notifier.db')
  with con:
    con.execute("""
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            date TEXT,
            locations TEXT
        );
    """)

def populate_dummy_data():
  sql = 'INSERT INTO USER (id, email, date, locations) values(?, ?, ?, ?)'
  data = [
      (1, 'testemail@gmail.com', '2021-09-01', '9'),
      (2, 'testemail2@hotmail.com', '2021-10-01', '9')
  ]
  con = sl.connect('notifier.db')
  with con:
    con.executemany(sql, data)