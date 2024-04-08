# Program to calculate the Simple Interest

amnt = int(input("Enter the principle amount:"))
year = int(input("Enter the number of years: "))
inte = int(input("Enter the rate of interest : "))
if (amnt and year and inte) > 0:
    SI = (amnt*year*inte)/100
    final = amnt + SI
print ("The interest on your sum is: ",amnt)
print ("The total amount is: ",final)
