#Bubble Sort

List1 = eval(input("Write list of numbers: "))
for i in range (len(List1)-1):
    for j in range (len(List1)-1-i):
        if List1[j] > List1[j+1]:
            List1[j] , List1[j+1] = List1[j+1], List1[j]
print ("After sorting: ",List1)
