import mysql.connector
myDB = mysql.connector.connect(
    host = "localhost",
    user = "Artem",
    password = "290395Arty",
    database = "python"
)

myCursor = myDB.cursor()

sql = "INSERT INTO user VALUES (%s,%s,%s,%s)"
users  = [
    ( 1989 , 'Nastya' , 'ns89@gmail.com' , 'PRO'),
    ( 1994 , 'Alexei' , 'tortex94@gmail.com' , 'REGULAR')
]

myCursor.executemany(sql, users)
myDB.commit()
myCursor.execute("SELECT * FROM user")
result = myCursor.fetchall()
for i in result:
    print(i)
myDB.close()