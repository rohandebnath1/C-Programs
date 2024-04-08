#Products csv file - Taking input of Mobiles --> Add_Record
#Products csv file - Showing details of those whose price is more than 12000 --> Show_Record()

import csv

def Add_Record():
    f = open(r"E:\Python Files\Mobile.csv","w",newline = "")
    w = csv.writer(f)
    n = int(input("Enter the number of inputs: "))
    for i in range(n):
        ModelNo = int(input("Enter the model number: "))
        Modelname = input("Enter the Model Name: ")
        Price = int(input("Enter the price: "))
        s = [ModelNo,Modelname,Price]
        i+=1
        w.writerow(s)
    f.close()

Add_Record()

def Show_Record():
    f = open(r"E:\Python Files\Mobile.csv","r",newline = "")
    r = csv.reader(f,delimiter=",")
    for i in r:
        if int(i[2]) > 12000:
            print ("All records with price more than 12000 are:")
            print (i) 
    f.close()

Show_Record()