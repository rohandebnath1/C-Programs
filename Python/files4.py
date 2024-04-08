# Files 4

#WAP to open a file and count the number of words

pen = open(r"E:\Python Files\text 2.txt",'r')
r = pen.read()
w = r.split()
c = len(w)
print ("Number of Words: ",c)
pen.close()
