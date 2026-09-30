import sqlite3
import sys

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

def add_expenses(amount, category, note):
    conn = get_connection()
    conn.execute(
        "INSERT INTO expenses (amount, category, note) VALUES (?,?,?)",
        (amount, category, note)
    )
    conn.commit()
    conn.close()


create_table()
command = sys.argv[1]
if command == 'add':
    amount = float(sys.argv[2])
    category = sys.argv[3]
    note = ""
    if len(sys.argv) >4:
        note = sys.argv[4]
    add_expenses(amount, category, note)
    print('Added:', amount, category, note)

if command =='list':
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, amount, category, note FROM expenses ORDER BY id"
    ).fetchall()
    conn.close()
    if len(rows) == 0:
        print("No expenses yet.")
    else:
        for expense_id, amount, category, note in rows:
            print(f'{expense_id}. {amount:.2f}  {category}  {note}')

def get_total(category = None):
    conn = get_connection()
    if category is None:
        row = conn.execute("SELECT SUM(amount) FROM expenses").fetchone()
    else:
        row = conn.execute("" \
        "SELECT SUM(amount) FROM expenses WHERE category = ?",
        (category,),
        ).fetchone()
    conn.close()
    total = row[0]
    if total == None:
        total = 0
    return total

if command == 'total':
    if len(sys.argv)>2:
        category = sys.argv[2]
        total = get_total(category)
        print(f'Total for {category}: {total:.2f}')
    else:
        total = get_total()
        print(f'Total: {total:.2f}')

