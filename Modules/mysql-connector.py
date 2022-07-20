import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "P@ssw0rd@123",
    database = "Django"
)

cursor = mydb.cursor()
# cursor.execute("CREATE TABLE Customer (name VARCHAR(255),address VARCHAR(255))")
cursor.execute("SELECT * FROM Customer")
for i in cursor:
    print(i)

# print("Created")