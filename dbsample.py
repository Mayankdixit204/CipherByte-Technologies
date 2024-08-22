import mysql.connector as MyConn
mydb=MyConn.connect(host="localhost",user="root",password="1234")
print(mydb)
