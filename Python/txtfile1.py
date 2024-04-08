#code to write in text file and read 

def write():
    f = open("C:\Python Files\Text2.txt","w")
    s = input("Enter the data you want to enter: ")
    f.write(s)
    f.close()

def read():
    g = open("C:\Python Files\Text2.txt",'r')
    p = g.read()
    print ("The contents of the given text file is: ",p)
    g.close()

write()
read()