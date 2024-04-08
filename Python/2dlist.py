lst = []
r = int(input("How many rows?"))
c = int(input("How many colums?"))
for i in range(r):
    row = []
    for j in range(c):
        elem = int(input("Enter element"+str(i)+","+str(j)+":"))
        row.append(elem)
    lst.append(row)
print("List created is:",lst)
