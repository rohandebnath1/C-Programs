st = 'ThIssOut@Put1452'
s=''
q=''
x = st[0:9]
y = st[len(x)::]
s=y+x
s=s[::-1]
for i in s:
    if i.isupper():
        q=q+i.lower()
    elif i.islower():
        q=q+i.upper()
    elif i.isdigit():
        q=q+str(int(i)+2)
    else:
        q=q+'#'

print (q)
