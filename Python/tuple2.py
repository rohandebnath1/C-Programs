tup = eval(input("Enter for tuple input"))
t1 = tup[2:8:2]
t2 = tup[-3:-9:-2]
t3 = t2[::-1]
if t3==t1:
    print("The two tuples contain the same elements in reversed order.")
else:
    print("The two tuples contain different elements.")
    
