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
      (1, 'test@gmail.com', 'week', '9'),
      (2, 'test@gmail.com', 'all', '9'),
      (3, 'test@hotmail.com', 'week', '9'),
  ]
  con = sl.connect('notifier.db')
  with con:
    con.executemany(sql, data)
  
def drop_table():
  con = sl.connect('notifier.db')
  with con:
    con.execute('DROP TABLE USER')
