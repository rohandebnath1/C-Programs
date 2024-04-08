def func():
    a=8
    b=10
    globals()['a'] = a - globals()['b']
    globals()['b'] = b - globals()['a']
    a=b*3
    b=globals()['a']*globals()['b']
    print (a,b)
    return b

a=3
b=6
a = func()
print (a,b)
b = func()
print (a,b)
