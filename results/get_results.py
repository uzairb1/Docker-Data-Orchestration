import mysql.connector

conn = mysql.connector.connect(user = 'codetest', password = 'swordfish', host = 'mysql', port = '3306', database = 'codetest')
cursor = conn.cursor()
cursor.execute("select * from students")
result = cursor.fetchall()
conn.close()

