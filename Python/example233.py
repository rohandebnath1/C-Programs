s = "Cbse Exam 2019-2020"
print(s)
r=""
for i in s:
    if i.isupper():
        r+=(chr(ord(i)+1)).upper()
    elif i.islower():
        r+=(chr(ord(i)+1)).upper()
    elif i.isdigit():
        p=int(i)
        if p%2==0:
            p=0
        else:
            p=1
        r+=str(p)
    else:
        r=r+i
print(r)
