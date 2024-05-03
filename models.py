import sqlite3

# establish connection with SQLite database
def connect_db():
    conn = sqlite3.connect('assistants.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS assistants (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT,
                          mobile TEXT,
                          email TEXT,
                          salary REAL,
                          city TEXT,
                          country TEXT,
                          department TEXT,
                          role TEXT
                      )''')
    conn.commit()
    return conn
