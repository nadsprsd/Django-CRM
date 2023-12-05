import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'MySQLPassW0rd!'
)

#prepare a cursor object

cursorObject = database.cursor()

#create a database

cursorObject.execute("CREATE DATABASE solocom")

print("All Done!")