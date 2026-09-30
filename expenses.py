import sqlite3

DB_FILE = 'expenses.db'

def get_connection():
    return sqlite3.connect(DB_FILE)


def create_table():
    conn = get_connection()
    conn.execute(
        "CREATE TABLE IF NOT EXISTS expenses ("
        "id INTEGER PRIMARY KEY,"
        "amount REAL,"
        "category Text,"
        "note TEXT)"
    )
    conn.commit()
    conn.close()

create_table()
print("Database ready.")