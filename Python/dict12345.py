#WAP to create a dictionary namely Numerals from following two lists

#keys = ['One', 'Two', 'Three']
#values = [1,2,3]


keys = ['One', 'Two', 'Three']
values = [1,2,3]

Numerals = dict(zip(keys,values))
print ("Give two lists are: ", keys,values)
print ("Dictionary created with these lists is")
print (Numerals)
