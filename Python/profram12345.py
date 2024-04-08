st = ''
for i in range (97,123):
    st = st+chr(i)

st = st.upper()
st = st.lstrip('ABCDEFK')
st = st.rstrip('WXYZ')
a = st[:len(st)//2]
b = st[len(st)//2:]
b=b+a
z=''
for i in b:
    if ord(i)>=65 and ord(i)<=90:
        z=z+chr(ord(i)+27)

print (z)
