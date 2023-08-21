from SQLMaster import *

Ser = '127.0.0.1'
User = 'root'
Pw = 'Crack123.'
Db = 'parkcard'

create_database_query = 'CREATE DATABASE {}'
drop_database_query = 'DROP DATABASE {}'
drop_table_query = 'DROP TABLE {}'
create_table_users_query = """
CREATE TABLE IF NOT EXISTS usuarios (
  id INT PRIMARY KEY,
  uid INT UNIQUE,
  nombres VARCHAR(16) NOT NULL,
  apellidos VARCHAR(16) NOT NULL,
  dob DATE
  );
"""
create_table_recargas_query = """
CREATE TABLE IF NOT EXISTS recargas (
  id INT PRIMARY KEY,
  uid INT UNIQUE,
  nombres VARCHAR(16) NOT NULL,
  apellidos VARCHAR(16) NOT NULL,
  recarga INT(16) NOT NULL,
  dob DATE
  );
"""
create_table_coins_query = """
CREATE TABLE IF NOT EXISTS coins (
  id INT PRIMARY KEY,
  uid INT UNIQUE,
  nombres VARCHAR(16) NOT NULL,
  apellidos VARCHAR(16) NOT NULL,
  coins INT(16) NOT NULL,
  dob DATE
  );
"""

SQL = SQLMaster(Ser,User,Pw,Db)

def connect():
    con = SQL.create_db_connection()
    if con:
        return con
    else:
        con = SQL.create_connection()
        if con:
            a = SQL.Equery(create_database_query.format(Db))
            if a:
                SQL.close_connection()
                con = SQL.create_db_connection()
                return con

def erase_db():
    con = SQL.create_connection()
    a = SQL.Equery(drop_database_query.format(Db))
    return a

erase_db()
#connect()
#SQL.Equery(create_table_users_query)
#SQL.Equery(create_table_recargas_query)
#SQL.Equery(create_table_coins_query)


























'''
import pyodbc 

server = 'TUF-HANS' 
database = 'ParkCard' 
username = 'ParkPlayMaster' 
password = 'parkplay123' 

con = "DRIVER={ODBC Driver 18 for SQL Server};SERVER="+server+";DATABASE="+database+";ENCRYPT=no;UID="+username+";PWD="+password

def connect(s):
    cnxn = pyodbc.connect(s)
    cnxn.setencoding('utf-8')  # (Python 3.x syntax)
    return cnxn

cnxn = connect(con)
cursor = cnxn.cursor()
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()
'''