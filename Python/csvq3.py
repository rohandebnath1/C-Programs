#Creating csv file with header

import csv

f = open(r"E:\Python Files\csv5.csv","a",newline = "")
p = csv.writer(f,delimiter=",")
data = []
header= ['Roll No.','Name','Class','Section']
data.append(header)
for i in range(5):
    roll_no = int(input("Enter Roll Number : "))
    name = input("Enter Name : ")
    Class = input("Enter Class : ")
    Section = input("Enter Section : ")
    rec = [roll_no,name,Class,Section] 
    data.append(rec)
p.writerow(data)
f.close()