#Simple writing in a Text  File

def Write_file():
    p = open(r"E:\Python Files\Hello World45.txt","w")
    s = []
    n = int(input("Enter the number of imputs: "))
    for i in range(n):
        s = input("Enter a string: ")
        p.write(s)
    p.close()

Write_file()