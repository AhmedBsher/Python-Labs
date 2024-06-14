import sqlite3
try:
 database = 'D:\Coding\Python Labs\Lab 5\database.db'
 connection = sqlite3.connect (database)
 cursor = connection.cursor()
 print('Successfully Connected to SQLite')
 query = 'SELECT * FROM Midterm' 
 cursor.execute (query)
 records = cursor.fetchall ()
 print('The records at the table: ', records)
 cursor.close()
 connection.close()
except:
 print('Error while connecting to SQLite')
 connection.close()