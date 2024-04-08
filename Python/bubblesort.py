#Bubble sort

lst = [15,6,13,22,3,52,2]
print = ("Original list:",lst)
n = len(lst)
for i in range(n):
    for j in range(0,n-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j] #Swapping
print ("List after sorting: ",lst)
            
