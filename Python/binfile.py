#Binary file handling using python

import pickle
def bin_write():
    f = open("E:\Python Files\binfile2.dat","w")
    s = ["Hello this is a binary file writen in Python Editor"]
    pickle.dump(s)
    f.close()

def bin_read():
    g = open("C:\Users\Rohan Debnath\Desktop\124734.bin","r")
    a = pickle.read(g)
    print ("The contents of the binary file are: ",a)
    g.close()

#bin_read()
bin_write()
