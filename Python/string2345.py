s = input("Enter the string")
s = 0
for a in s:
    if a.isdigit():
        s = s + int(a)
print ("Sum of string's digit is", s)
