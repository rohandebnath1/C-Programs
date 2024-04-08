#Alternative way of opening a file

with open (r"C:\Python Files\Poem.txt","r") as f:
    a = f.readlines(400)
    print (a)
    