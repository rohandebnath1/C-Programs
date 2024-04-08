#to delete all prime numbers from a list

l = []
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

size = int(input("No. of elements:"))
for i in range(size):
    l.append(int(input("Enter any integer no.:")))

c=0
while c<size:
    if prime(l[c]):
        l.pop(c)
        size=size-1
    else:
        c=c+1
print("List without prime numbers:",l)
