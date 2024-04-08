import mysql.connector as mycon
sql = mycon.connect(host = "localhost",user = "root",password = "root")
if sql.is_connected():
    print ("Connection Established")
else:
    print ("Connection Failed")
sql.close()
    
