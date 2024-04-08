import random as rd

pick = rd.randint(0,3)
city = ["DELHI","KOLKATA","MUMBAI","CHENNAI"]
for i in city:
    for j in range(1,pick):
        print (i,end=" ")
    print()
