import pickle
names = ['First','Second','Third','Fourth','Fifth']
lst = []
for i in range (-1,-5,-1):
    lst.append(names[i])
with open('test.dat','wb') as fout:
    pickle.dump(lst,fout)
with open('test.dat','rb') as fin:
    nlist = pickle.load(fin)
print(nlist)
