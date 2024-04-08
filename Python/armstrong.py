sum1 = 0
c = 0
num = int(input("Enter a number: "))
temp = num
while(temp!=0):
    temp = temp // 10
    c += 1

temp = num
print("Total digs are: ",c)

while (temp != 0):
    a = temp % 10
    temp = temp // 10
    b = a**c
    sum1 = sum1 + b

if (sum1==num):
    print("Its an Armstrong number!")
else:
    print("Not an Armstrong Number")


