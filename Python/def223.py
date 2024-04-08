val = 100
def display(N):
    global val
    val = 50
    if N%14==0:
        val=val+N
    else:
        val=val-4
print (val,end="@")
display(40)
print(val)
