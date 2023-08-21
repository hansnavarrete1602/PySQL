import mysql.connector
from mysql.connector import Error

class SQLMaster:
    def __init__(self,ser,user,pw,database):
        self.servidor = ser
        self.usuario = user
        self.clave = pw
        self.db = database
        self.connection = None
    
    def create_connection(self):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=self.servidor,
                user=self.usuario,
                passwd=self.clave
            )
        except Error as err:
            return err
        return self.connection
    
    def close_connection(self):
        self.connection.close()
    
    def create_db_connection(self):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=self.servidor,
                user=self.usuario,
                passwd=self.clave,
                database=self.db
            )
        except Error as err:
            return False
        return self.connection
    
    def Equery(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            return True
        except Error as err:
            return err
        
    def Rquery(self, query):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            return err
        
    def Lquery(self, sql, val):
        cursor = self.connection.cursor()
        try:
            cursor.executemany(sql, val)
            self.connection.commit()
            return True
        except Error as err:
            return err