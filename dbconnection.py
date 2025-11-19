# dbconnection.py
import pymysql

def get_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Aaska@@',
        database='mydb'
    )
    return conn