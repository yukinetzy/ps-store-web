import sqlite3
from config import DB_PATH

def add_test_products():
    conn = sqlite3.connect(DB_PATH)
    curs = conn.cursor()

    test_products = [
        ("FIFA 23", 1999, "TR"),
        ("God of War", 2499, "IN"),
        ("Spider-Man", 3499, "TR")
    ]

    curs.executemany('INSERT INTO products (name, price, region) VALUES (?, ?, ?)', test_products)
    conn.commit()
    conn.close()