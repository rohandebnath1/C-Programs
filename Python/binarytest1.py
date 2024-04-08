import pickle

def binary_file():
    f = open ("E:\Python Files\Okbin.txt","wb")
    s = "Hope u could read this.."
    pickle.dump(s,f)
    f.flush()
    f.close()
    print ("Data inserted successfully!")

binary_file()

def write_inp():
    v = 0
    g = open ("E:\Python Files\ok2.txt","w")
    while True:
        s = input("Enter Text: ")
        g.write(s)
        d = input("Do you want to continue(y/n): ")
        if d!= "Yy":
            break
    g.close()
write_inp()

def read_len():
    v = 0
    h = open ("E:\Python Files\Ok3.txt","r")
    for i in h:
        for j in i:
            s = len(j)
            s = s + v
            v+=1
            d = v
            print ("Total Words:", d)
    h.close()
read_len()
 