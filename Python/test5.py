L = eval(input("Enter list to sort:"))
for i in range(1,len(L)):
    n=L[i]
    j = i - 1
    while j >= 0 and n<L[j]:
        L[j+1] = L[j]
        j = j-1
    L[j+1] = n
print(n)
