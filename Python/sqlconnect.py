import mysql.connector as con

mycon = con.connect(
    host = "localhost",
    username = "root",
    password = "12345")
while mycon.is_connected():
    print ("Connection Successfull")

cur = mycon.cursor()
Q = "show databases"
b = cur.execute(Q)
print (b)