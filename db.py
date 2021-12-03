import sqlite3 as sl

def setup():
  con = sl.connect('notifier.db')
  with con:
    con.execute("""
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            email TEXT
        );
    """)

def populate_dummy_data():
  sql = 'INSERT INTO USER (id, email) values(?, ?)'
  data = [
      (1, 'test@msg.telus.com'),
      (2, 'test@gmail.com'),
      (3, 'test@hotmail.com'),
  ]
  con = sl.connect('notifier.db')
  with con:
    con.executemany(sql, data)
  
def drop_table():
  con = sl.connect('notifier.db')
  with con:
    con.execute('DROP TABLE USER')
