#to calculate the frequency of a list

lst = eval(input("Enter list:"))
length = len(lst)
element = int(input("Enter element: "))
count = 0
for i in range(0,length):
    if element == lst[i]:
        count+=1
if count==0:
    print(element,"not found in given list")
else:
    print(element,"has frequency as",count,"in given list")
    
