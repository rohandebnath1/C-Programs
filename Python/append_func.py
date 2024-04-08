#To take list input without using eval function

l =[]
n = int(input("Enter the number of elements: "))

for i in range(0,n):
    l.append(input("Enter anything:"))
print (l)
