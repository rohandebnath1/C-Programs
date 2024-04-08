M = {}
n = int(input("How many students:"))
for a in range(n):
    r,m = eval(input("Enter Roll No.,Marks:"))
    M[r] = m
print ("Created Dictionary")
print (M)
ans = 'y'
while ans == 'y':
    print ("Enter details of new students: ")
    r,m = eval(input("Roll No.,Marks:"))
    M[r] = m
    ans = input("More students? (y/n):")
print ("Dictionary after adding new students")
print(M)
