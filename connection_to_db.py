import sqlite3
from mmap import error
def connect_db():
    conn = sqlite3.connect('new1.db')
    c = conn.cursor()
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS category(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category VARCHAR);
    """)
    except sqlite3.DatabaseError as error:
        print("ERROR",error)
    conn.commit()
    conn.close()



"""добовление в базу категорий"""

def insert_category_db(item):
    connect_db()
    conn = sqlite3.connect('new1.db')
    c = conn.cursor()
    if item !="":
        try:
            c.execute("""INSERT INTO category(id,category) values(NULL,?);""",(item.capitalize(),))
        except sqlite3.DatabaseError as error:
            print('ERROR',error)
        conn.commit()
        conn.close()

"""выбор из базы категорий"""

"""def fetch_all():
    conn = sqlite3.connect('new1.db')
    c = conn.cursor()
    c.execute("select * from category;")
    all_result = c.fetchall()
    return all_result"""

