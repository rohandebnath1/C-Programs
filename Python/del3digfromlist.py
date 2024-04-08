#to delete all 3 digit numbers from list

l = []
def count_dig(n):
    c=0
    while n!=0:
        n=n//10
        c+=1
    return c

size = int(input("No. of elements:"))
for i in range(size):
    l.append(int(input("Enter anything: ")))

c=0
while c<size:
    if count_dig(l[c]==3):
                l.pop(c)
                size -= size
    else:
        c+=1
print("The list without three digit numbers:",l)

        
