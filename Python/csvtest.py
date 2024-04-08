import csv 
import os
f = open(r"E:\Python Files\Train.csv","r")
g = open(r"E:\Python Files\Temp.csv","w",newline = "")
rea = csv.reader(f)
wri = csv.writer(g)
pnr = int(input("Enter your PNR Number: "))
for row in rea:
    if row[3] != pnr:
        wri.writerow(row)
    else:
        del(row)
        
f.close()
g.close()