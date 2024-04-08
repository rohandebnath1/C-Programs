import csv
import pickle
import os

def convert():
    f = open(r"E:\Python Files\test2.csv","r")
    g = open(r"E:\Python Files\test3.dat","wb")
    p = csv.reader(f,delimiter=",")
    for i in p:
        pickle.dump(str(i),g)
    f.close()
    g.close()
    os.remove("test2.csv")
    os.rename("test3.dat","test2.dat")

convert()

#Checking

f = open(r"E:\Python Files\test3.dat","rb")
r = pickle.load(f)
print(r)
f.close()
