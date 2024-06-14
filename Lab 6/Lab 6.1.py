import sqlite3

name = "D:\\Coding\\Python Labs\\Lab 6\\weather.txt"
handle = open(name, 'r')

try:
    database = "D:\\Coding\\Python Labs\\Lab 6\\NewDatabase.db"
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    print("Successfully Connected to SQLite")

    delete_query = "DELETE FROM weather"
    cursor.execute(delete_query)

    for line in handle:
        columns = line.split()

        date = columns[0]
        day = columns[1]
        temp = columns[2]
        status = columns[3]

        query = "INSERT INTO weather VALUES('" + date + "','" + day + "','" + temp + "','" + status + "')"
        cursor.execute(query)

        print("Successfully inserted weather data of: ", date)

    cursor.close()
    connection.close()

except sqlite3.Error as error:
    print("Error while connecting to SQLite", error)
    connection.close()