'''#print only the capital vowel letters

s = input("Enter the statement")
wd = s.split()

for i in wd:
    if i[0] in ['A','E','I','O','U']:
        print ("Capital vowel letters are:",i)
print()'''

#Double vowel words
        
z = input("Enter a sentence")
m = ('aa' 'ee' 'ii' 'oo' 'uu' 'Aa' 'Ee' 'Ii' 'Oo' 'Uu' 'ae' 'ai' 'ao' 'au' 'Ea' 'Ei' 'Eo' 'Eu' 'Ia' 'Ie' 'Io' 'Iu' 'Oa' 'Oe' 'Oi' 'Ou' 'Ua' 'Ue' 'Ui' 'Uo') 
wd = z.split() 
for i in wd:
    if i[0] in m:
        print ("Double vowels words",i)



