#Pattern --> Reverse Pyramid of numbers

n = int(input("Enter the number of rows: "))
for i in range(1,n):
    for j in range(i,0,-1):
        print(j,end="")
    print("")
    
