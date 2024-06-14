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
        temperature = columns[2]
        status = columns[3]

        query = f"INSERT INTO weather (date, day, temperature, status) VALUES ('{date}', '{day}', '{temperature}', '{status}')"
        cursor.execute(query)

        print("Successfully inserted weather data of: ", date)

    cursor.close()
    connection.commit()
    connection.close()

except sqlite3.Error as error:
    print("Error while connecting to SQLite", error)
    if connection:
        connection.close()

# New part to search for weather data by date
try:
    database = "D:\\Coding\\Python Labs\\Lab 6\\NewDatabase.db"
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    
    date_input = input("Enter the date to search for weather information : ")
    
    search_query = f"SELECT * FROM weather WHERE date = '{date_input}'"
    cursor.execute(search_query)
    result = cursor.fetchone()
    
    if result:
        print(f"Weather data for {date_input}:")
        print(f"Date: {result[0]}, Day: {result[1]}, Temperature: {result[2]}, Status: {result[3]}")
    else:
        print(f"No data available for the date: {date_input}")
    
    cursor.close()
    connection.close()

except sqlite3.Error as error:
    print("Error while connecting to SQLite", error)
    if connection:
        connection.close()