#Insertion Sort

lst = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    a = int(input("Enter elements: "))
    lst.append(a)

#Sorting
    
print ("Original List:",lst)
for i in range(1,len(lst)):
    key = lst[i]
    j=i-1
    while j>=0 and key < lst[j]:
        lst[j+1] = lst[j]
        j = j - 1
    else:
        lst[j+1] = key
print ("After sorting",lst)
