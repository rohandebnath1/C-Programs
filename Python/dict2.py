def myFunction(x,p):
    t = x[p]
    for i in range (p,-1,-1):
        x[i]=x[i-1]
    x[0]=t

a = [1,5,7,19,2,18,6]
for i in range (2,5):
    myFunction(a,i)
print(a)





    
