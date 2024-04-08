s = "Cbse Exam 2019-2020"
print (s)
r=""
for i in s:
    if i.isupper():
        r+=(chr(ord(i)+1)).upper()
    elif i.islower():
        r+=(chr(ord(i)+2)).upper()
    elif i.isdigit():
        r+=str(int(i)+1)
    else:
        r=r+i
print(r)