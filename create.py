import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to a SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
   except Error as e:
       print(e)
   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

if __name__ == '__main__':
         
   create_zadania_sql = """
   -- zadania table
   CREATE TABLE IF NOT EXISTS zadania (
      id integer PRIMARY KEY,
      tytuł text NOT NULL,
      opis text NOT NULL,
      czy_zrobione bool
   );
   """
   db_file = "db.sqlite"

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_zadania_sql)
       conn.close()