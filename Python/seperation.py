#seperating positive and negative numbers

val =[]
n = int(input("Enter the number of elements: "))

for i in range(0,n):
    val.append(input("Enter anything:"))

plist = []
nlist = []
s = len(val)
for i in range (s):
    if val[i]<0:
        nlist.append(val[i])
    elif val[i]>0:
        plist.append(val[i])
print("Main list: ",val)
print("Positive numbers list: ",plist)
print("Negetive numbers list: ",nlist)
