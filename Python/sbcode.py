import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os
import platform
def clrscreen():
        if platform.system()=="Windows":
                print(os.system("cls"))
 
def display():
    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user='root', passwd='mysql', host='localhost', database='Library')
        Cursor = cnx.cursor()
        query = ("SELECT * FROM BookRecord")
        Cursor.execute(query)
        for (Bno,Bname,Author,price,publ,qty,d_o_purchase) in Cursor:
            print("========================================")
            print("Book Code : ",Bno)
            print("Book Name : ",Bname)
            print("Author of Book : ",Author)
            print("Price of Book : ",price)
            print("Publisher : ",publ)
            print("Total Quantity in Hand : ",qty)
            print("Purchased On : ",d_o_purchase)
            print("============================================")
        Cursor.close()
        cnx.close()
        print("You have done it!!!!!!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
display()