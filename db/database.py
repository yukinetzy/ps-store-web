import sqlite3
from config import DB_PATH


def get_conn():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = sqlite3.connect(DB_PATH)
    curs = conn.cursor()

    # Таблица пользователей
    curs.execute('''CREATE TABLE IF NOT EXISTS users 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   user_id INTEGER UNIQUE,
                   username TEXT, 
                   password TEXT)''')

    # Таблица товаров
    curs.execute('''CREATE TABLE IF NOT EXISTS products
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   price REAL,
                   region TEXT)''')

    # Таблица корзины
    curs.execute('''CREATE TABLE IF NOT EXISTS cart
                   (user_id INTEGER,
                   product_id INTEGER,
                   FOREIGN KEY(user_id) REFERENCES users(user_id),
                   FOREIGN KEY(product_id) REFERENCES products(id))''')

    # Таблица заказов
    curs.execute('''CREATE TABLE IF NOT EXISTS orders 
                   (id INTEGER PRIMARY KEY,
                   user_id INTEGER,
                   total REAL,
                   status TEXT,
                   region TEXT,
                   timestamp DATETIME)''')

    # Таблица подписок
    curs.execute('''CREATE TABLE IF NOT EXISTS subscriptions 
                   (user_id INTEGER,
                   type TEXT,
                   start_date DATETIME,
                   end_date DATETIME)''')

    # Таблица промокодов
    curs.execute('''CREATE TABLE IF NOT EXISTS promocodes 
                   (code TEXT PRIMARY KEY,
                   discount REAL)''')
    conn.commit()
    conn.close()
