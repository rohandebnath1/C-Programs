import csv
f = open(r"Python Files/Train.csv","r")
g = csv.reader(f)
for i in g:
    print (i)   
f.close()
 
 