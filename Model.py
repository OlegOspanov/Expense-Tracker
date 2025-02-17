from itertools import count

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import insert,select

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

metadata.create_all(engine)

"""создание базы продуктов"""
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
        print(f'выбор из базы {a}')
        return a



def fletch_products_category(item):
    select_query = select(Products)
    print(item)
    with engine.connect() as connection:
        result = connection.execute(select_query)
        rows = result.fetchall()
        print(rows)
        for i in rows:
            if i[1] == item:
                print(i[1])
                category = i[3]
                print(category)
                return category



