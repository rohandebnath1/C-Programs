#Files 1
'''
#Read 

pen = open (r"E:\Python Files\Hello World.txt")
print (pen.read())
pen.close()

'''
#Write

pen = open (r"E:\Python Files\Hello World.txt",'r')
for i in range (5):
    nm = input("Enter student name: ")
    pen.write(nm)
    pen.write('/n')
pen.close()
