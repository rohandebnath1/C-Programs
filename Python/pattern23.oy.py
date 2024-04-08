#pattern with number of lines in input

n = int(input("Enter the number of lines: "))
s = n
for i in range(1,n+1):
    for k in range (1,s+1):
        print(" ",end = "")
    for j in range (1,i+1):
        print("*",end="")

    print()
    s = s-1

s = n - 1
for i in range(1,n+1):
    for k in range(1,i+1):
        print(" ",end="")
    for j in range(1,s+1):
        print("*",end="")

    print()
    s=s-1
    
