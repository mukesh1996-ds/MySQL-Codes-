import mysql.connector

# Connection 

conn = mysql.connector.connect(
    host = 'localhost',
    password = '12345',
    user = 'root'
)

# Checking connection

if conn.is_connected():
    print("Connection Established....")