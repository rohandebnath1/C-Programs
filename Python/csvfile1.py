#Fully Working : CSV read and write data

# Show Records of a csv file

import csv

def Input_rec():
    f = open(r"/home/rohan/Python Files/Records_1.csv","w",newline = "")
    w = csv.writer(f,delimiter=",")
    n = int(input("Enter the number of inputs: "))
    for i in range(n):
        Pid = int(input("Enter Product ID: "))
        Pname = input("Enter the product name: ")
        Mfg = input("Enter the Mfg Date: ")
        Price = int(input("Enter the price: "))
        P = [Pid,Pname,Mfg,Price]
        w.writerow(P)
        i+=1
    f.close()

#Input_rec()
    

def show_record():
    f = open(r"/home/rohan/Python Files/Records_1.csv","r",newline="")
    r = csv.reader(f)
    for c in r:
        print("Product Id: ",c[0])
        print("Name of the product: ",c[1])
        print("Manufacture Date: ",c[2])
        print("Price of the product: ",c[3])
    f.close() 

show_record()