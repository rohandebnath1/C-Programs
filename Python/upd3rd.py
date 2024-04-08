#To update the nth element from a list

L = []
N = int(input("Enter how many numbers: "))
for i in range (N):
    L.append(int(input("Enter the values: ")))

x = int(input("Enter the value: "))
n = int(input("Enter the position: "))
L = L[0:n-1]+[x]+L[n-1:]
print (L)

