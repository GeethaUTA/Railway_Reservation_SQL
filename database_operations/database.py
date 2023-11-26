# database.py
import sqlite3

def create_connection():
    conn = sqlite3.connect('railway_reservation.db')
    return conn

def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
