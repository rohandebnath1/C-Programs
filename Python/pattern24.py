#hollow pattern --> Triangle

n = int(input("Enter number of lines: "))
s=n
for i in range (1,n+1):
    for k in range(1,i+1):
        print(" ",end="")
    for j in range(1,s+1):
        if i==1 or j==1 or j==s:
            print("* ",end="")
        else:
            print("  ",end="") #three blank spaces

    print()
    s=s-1
            
