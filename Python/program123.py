x = 'LockDownCOVID19-2020'
y = ''
z = ''
i = 0
k = x.lstrip('Lock')
while i<len(x):
    y = x[i:]
    z = x[-len(x):-i]
    i+=1
    
y = y+k+z
z = ''
k = ''
for j in y:
    if j.isupper():
        z=z+j.lower()
    elif j.isdigit():
        k=k+str(int(j)+5)
    else:
        z=z+j
z=z+k
print (z)
