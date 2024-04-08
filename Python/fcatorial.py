#To find the factorial of a number

n = int(input("Entera number: "))
fac = 1
if n<0:
    print ("Sorry, factorial does not exist for negetive number"))
elif n ==0:
    print ("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fac = fac * i
    print ("The factorial of",num,"is",fac)
