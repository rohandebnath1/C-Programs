#Find the output 

def sample1(n,m):
    f = n>m and n or m
    if f%2 == 0:
        return f + m
    else:
        return f + n
def sample2(a,b,c=10):
    globals()['a'] = b + sample1(a,c)
    b = globals()['b'] + a + sample1(a,b)
    c = a + b
    print (a,b,c)
    return c

a = 10
b = 8
c = 12
c = sample2(a,b,c)
print(a,b,c)