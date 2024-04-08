import csv
f = open(r"C:\Python Files\File5.csv","w")
wri = csv.writer(f)
n = int(input("Enter number of inputs: "))
for i in range(n):
    itm_no = int(input("Enter Item Number: "))
    name = input("Enter Customer Number: ")
    itm_nm = input("Enter Item Name: ")
    dom = input("Enter date of manufacturing: ")
    h = [itm_no,name,itm_nm,dom]
    wri.writerow(h)
f.close()

    

