myfile = open(r"E:\Python Files\File2.txt")
x = myfile.read()
y = x.count('the')
print(y)
myfile.close()