import csv

def Show_Record():
    f = open(r"C:\Python Files\phdir.csv","r",newline = "")
    r = csv.reader(f,delimiter=",")
    for i in r:
        print(i)
    f.close()
Show_Record()
