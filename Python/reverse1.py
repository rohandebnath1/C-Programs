#reverses the list in place Type 2

val = eval(input("Enter a list:"))
print ("Original list:",val)
s=len(val)
mid=s//2
neg=-1
for i in range(mid):
    val[i],val[neg]=val[neg],val[i]
    neg=-1
print("Reversed list:",val)
