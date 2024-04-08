#Fully functional Binary READ and WRITE Data 


import pickle

def add_rec():
    f = open(r"C:\Python Files\products2.dat","wb")
    Pno = int(input("Enter the Product Number: "))
    Product_name = input("Enter Product name: ")
    MFG_Date = input("Enter manufacture date: ")
    Price = int(input("Enter product price: "))
    s = [Pno,Product_name,MFG_Date,Price]
    pickle.dump(s,f)
    f.close()

def ShowRecord():
    f = open(r"C:\Python Files\products2.dat","rb")
    try:
        while True:
            d = pickle.load(f)
            print(d)
    except EOFError:
        print ("File End")
        f.close()
#add_rec()
ShowRecord()