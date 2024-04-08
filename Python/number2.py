n = input("Enter Number: ")
s = n[::-1]
k = 0
w = 0
for i in s:
    w = w + (int(i) * (2**k))
    k += 1
print (w)
