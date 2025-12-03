import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",              
        password="KARTIK_2004", 
        database="capstone_db"
    )
