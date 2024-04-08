#Direct method
Dict = eval(input("Enter a dictionary"))
print ("The dictionary is:",Dict)

#Using loop

d = {}
n = int(input("How many values: "))
for i in range (n):
    key = eval(input("Enter the key: "))
    val = eval(input("Enter the values: "))
    d[key]=val
print ("The dictionary created is: ",d)

#Using functions

key = eval(input("Enter the keys:"))
value = eval(input("Enter the value"))
d = dict(zip(key,value))
print ("The Dictionary is:", d)


