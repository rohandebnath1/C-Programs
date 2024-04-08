#to del all duplicate numbers from a list

L = []
n = int(input("Enter how many numbers: "))
for i in range (n):
    L.append(int(input("Enter the values: ")))
print ("Before modification:")
print (L)
ln=len(L)
i=0
while i<ln:
    x=L[i]
    j=i+1
    while j<ln:
        if x==L[j]:
            del L[j]
            ln=len(L)
            j=j+1
        else:
            j+=1
    i+=1
print ("After modification:")
print (L)
