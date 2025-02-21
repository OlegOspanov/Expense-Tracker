from itertools import count
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import insert,select
from sqlalchemy.orm import sessionmaker

from collections import Counter

metadata = MetaData()
engine = create_engine('sqlite:///ExTrac.db')


Products = Table(
    'Products', metadata,
    Column('id', Integer, primary_key=True),
    Column('Product', String),
    Column('Price', String),
    Column('Category',String)
)

Categorys = Table(
    'Categorys', metadata,
    Column('id', Integer, primary_key=True),
    Column('Category',String)
)


metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

"""добовление базы продуктов"""
def insert_db(name,num,value):
    insert_query = insert(Products).values(Product=name.capitalize(),Price=num,Category=value)
    with engine.connect() as connection:
        connection.execute(insert_query)
        connection.commit()

"""выбор за базы продуктов"""
def fletch_products_name():
    select_query = select(Products)
    with engine.connect() as connection:
        result = connection.execute(select_query)
        rows = result.fetchall()
        sorted_list = [i[1] for i in rows]
        a = Counter(sorted_list).most_common(15)
        return a

def fletch_products_price(item):
    select_query = select(Products)
    with engine.connect() as connection:
        result = connection.execute(select_query)
        rows = result.fetchall()
        sorted_list = [i[2] for i in rows if i[1]==item]
        a = Counter(sorted_list).most_common(1)
        return ''.join([i[0] for i in a])


def fletch_products_category(item):
    select_query = select(Products)
    with engine.connect() as connection:
        result = connection.execute(select_query)
        rows = result.fetchall()
        for i in rows:
            if i[1] == item:
                category = i[3]
                return category



"""добовление таблицы категорий"""
def insert_db_category(name):
    insert_query = insert(Categorys).values(Category=name.capitalize())
    with engine.connect() as connection:
        connection.execute(insert_query)
        connection.commit()



"""выбор из базы категорий"""
def fetch_all():
    select_query = select(Categorys)
    with engine.connect() as connection:
        result = connection.execute(select_query)
        rows = result.fetchall()
        return rows

class Total():
    def get_total(self):
        select_query = select(Products)
        with engine.connect() as connection:
            result = connection.execute(select_query)
            rows = result.fetchall()
            a = [int(i[2]) for i in rows]
            return sum(a)

