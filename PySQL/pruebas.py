from SQLMaster import *
import pandas as pd
import datetime

Ser = '127.0.0.1'
User = 'root'
Pw = 'Crack123.'
Db = 'card_db'

create_database_query = 'CREATE DATABASE {}'
drop_database_query = 'DROP DATABASE {}'
drop_table_query = 'DROP TABLE {}'
create_table_users_query = '''
CREATE TABLE IF NOT EXISTS users (
  id INT PRIMARY KEY,
  uid VARCHAR(12) NOT NULL,
  nombres VARCHAR(16) NOT NULL,
  apellidos VARCHAR(16) NOT NULL,
  fecha VARCHAR(12) NOT NULL
  );
'''
create_table_money_query = '''
CREATE TABLE IF NOT EXISTS charges (
  id INT PRIMARY KEY,
  uid VARCHAR(12) NOT NULL,
  nombres VARCHAR(16) NOT NULL,
  apellidos VARCHAR(16) NOT NULL,
  recarga INT(16) NOT NULL,
  fecha VARCHAR(12) NOT NULL
  );
'''
create_table_coins_query = '''
CREATE TABLE IF NOT EXISTS coins (
  id INT PRIMARY KEY,
  uid VARCHAR(12) NOT NULL,
  nombres VARCHAR(16) NOT NULL,
  apellidos VARCHAR(16) NOT NULL,
  coins INT(16) NOT NULL,
  fecha VARCHAR(12) NOT NULL
  );
'''
read_all_table_query = '''
SELECT * FROM {};
'''
insert_users_query = '''
INSERT INTO {} VALUES
(%s,%s,%s,%s,%s);
'''

SQL = SQLMaster(Ser, User, Pw, Db)


def connect():
    con = SQL.create_db_connection()
    if con:
        SQL.Equery(create_table_users_query)
        SQL.Equery(create_table_money_query)
        SQL.Equery(create_table_coins_query)
        return con
    else:
        con = SQL.create_connection()
        if con:
            a = SQL.Equery(create_database_query.format(Db))
            if a:
                SQL.close_connection()
                con = SQL.create_db_connection()
                SQL.Equery(create_table_users_query)
                SQL.Equery(create_table_money_query)
                SQL.Equery(create_table_coins_query)
                return con


def erase_db():
    SQL.create_connection()
    a = SQL.Equery(drop_database_query.format(Db))
    return a


def add_user(size,uid,name,surname):
    now = datetime.datetime.now()
    val = [(size, f'{uid}', f'{name}', f'{surname}', now.strftime('%d-%m-%Y'))]
    a = SQL.Lquery(insert_users_query.format('users'), val)
    return a


def read_table(tb):
    from_db = []
    read = SQL.Rquery(read_all_table_query.format(tb))
    for result in read:
        result = list(result)
        from_db.append(result)
    columns = ['ID', 'UID', 'Name', 'Surname', 'Date Creation']
    df = pd.DataFrame(from_db, columns=columns)
    return df


#erase_db()
#'''
connect()
read = read_table('users')
size = len(read) + 1
uid = 'EC C6 7B 2A'
name = 'Hans Sebastian'
surname = 'Navarrete Lopez'
add_user(size,uid,name,surname)
read = read_table('users')
print(read)
SQL.close_connection()
#'''