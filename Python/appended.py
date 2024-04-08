#to append a list

myl = [2,4,6]
print("Existing list:",myl)
n=eval(input("Enter a number or a list to be appended:"))
if type(n)==type([]):
    myl.extend(n)
elif type(n) == type(1):
    myl.append(n)
else:
    print("Please enter either an integer or a list:")
print("Appended list is:",myl)

