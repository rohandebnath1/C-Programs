#Sample csv read and write data

import csv 

def Addproduct(pid,pname,price):
    f = open(r"E:\Python Files\Product.csv","w")
    p = csv.writer(f)
    p.writerow([pid,pname,price])
    f.close()

def Readproduct():
    f = open(r"E:\Python Files\product.csv","r")
    p = csv.reader(f)
    for row in p:
        print ("Product ID: ",row[0])
        print ("Product name ",row[1])
        print ("Product Price: ",row[2])
    f.close()

Addproduct("M102","Mouse","450")
Addproduct("M103","Pen","250")
Addproduct("M104","Bag","650")
Readproduct()