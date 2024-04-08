#removing duplicates

val = eval(input("Enter a list:"))
tmp = []
print ("Original list is:",val)
for a in val:
    if a not in tmp:
        tmp.append(a)
val = list(tmp)
print ("List after removing duplicates:",val)
    
