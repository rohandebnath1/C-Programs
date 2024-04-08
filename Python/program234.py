def Sample1(a,b):
    global x
    a=b+x
    x=a-b
    return a
def Sample2(m):
    x=2
    y=3
    globals()['x']=Sample1(x,y)+Sample1(y,x)
    return y
x=10
y=20

x=Sample1(x,y)
print(x,y)

y=Sample2(x)
print(x,y)
