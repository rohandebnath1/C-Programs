import csv

def Insert_rec():
    Q = "Yy"
    f = open(r"E:\Python Files\product2.csv","a",newline = "")
    w = csv.writer(f,delimiter=",")
    while Q == "Yy":
        pno = int(input("Enter Product Number: "))
        pname = input("Enter Product name: ")
        mfg = input("Enter manufacturing date: ")
        price = int(input("Enter the price of the prodict: "))
        p = [pno,pname,mfg,price]
        Q = input("Do you want to add more values: (Y/N)")
        w.writerow(p)
        f.close()

Insert_rec()

def Show_rec():
    f = open(r"E:\Python Files\product2.csv","r")
    w = csv.reader(f,delimiter=",")
    for  i in w:
        print (i)
    f.close()

Show_rec()

