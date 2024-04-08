import csv
import random 
import os

def railresmenu():
    print("==Welcome to Railway reservation==")
    print()
    print("1. Show available train lists: ")
    print("2. Train Reservation")
    print("3. Cancel Ticket")
    print("4. Check PNR Status")
    print("5. Edit your ticket details")
    print("6. Show tickets")
    print("7: Exit Menu")
    print()
    n = int(input("Enter your choice: "))
    if (n==1):
        trainlist()
    elif (n==2):
        print ("=+=+=+=+=+=+=+= Enter the credentials please: =+=+=+=+=+=+=+=")
        creds()
    elif (n==3):
        print ("=+=+=+=+=+=+=+= Enter PNR for cancellation: =+=+=+=+=+=+=+=")
        CancelTicket()
    elif (n==4):
        PNRStatus()
    elif (n==5):
        Edit()
    elif (n==6):
        ShowTicket()
    elif (n==7):
        print("Have a great day!! ")
    else:
        print("Wrong Choice")
        railresmenu()
    

def trainlist():
    print("=+=+=+=+=+=+=+= Trains available =+=+=+=+=+=+=+=")
    print("=+           Delhi ----> Mumbai               =+")
    print("=+          Mumbai ----> Chennai              =+")
    print("=+           Delhi ----> Kolkata              =+")
    print("=+         Kolkata ----> Bangalore            =+")
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    print()
    print()
    railresmenu()

data = []
class details:
    def creds():
        f = open(r"/home/rohan/Python Files/Train.csv","a")
        cv=csv.writer(f)
        L = []
        date = input("Enter date of travel dd/mm/yyyy: ")
        number = int(input("Enter the number of passengers: "))
        for i in range(number):
            name = input("Enter your name: ")
            age = int(input("Enter Age: "))
            Lf = [name,age]
            L.append(Lf)
        class_1 = int(input("Enter the choice for class: \n 1.General \n 2.AC 1st Tier \n 3.AC 2nd Tier \n 4.AC 3rd Tier ---> "))
        if class_1 == 1:
            g = "General Class"
        elif class_1 == 2:
            g = "AC First Tier"
        elif class_1 == 3:
            g = "AC Second Tier"
        elif class_1 == 4:
            g = "AC Third Tier"
        def pnr(n):
            range_start = 10**(n-1)
            range_end = (10**n)-1
            return random.randint(range_start, range_end)
        pnr_number = pnr(10)
        print ("Your PNR Number: ",pnr_number)

        def price():
            if class_1 == 1:
                p = random.randrange(600,1000)
            elif class_1 == 2:
                p = random.randrange(1800,2300)
            elif class_1 == 3:
                p = random.randrange(1300,1800)
            elif class_1 == 4:
                p = random.randrange(1100,1500)
            pr = (p + (5/100)*p) 
            return pr
        fare = price()
        fareall = price()*number
        pnrstatus = "Booked"
        print ("Your fare per person = Rs",fare)
        print ("Your total fare (inclusive of tax) = Rs", fareall)

        cred = [date,L,g,pnr_number,fareall,pnrstatus]
        f = open(r"/home/rohan/Python Files/Train.csv","a",newline = "")
        cv.writerow(cred)
        f.close()
        print("\n +=+=+=+=+=+=Returning to Menu+=+=+=+=+=+= ")
        railresmenu()


def CancelTicket():
    f = open(r"/home/rohan/Python Files/Train.csv","r")
    g = open(r"/home/rohan/Python Files/Temp.csv","w",newline="")
    reader = csv.reader(f)
    writer = csv.writer(g)
    pnr = input("Enter your PNR Number: ")
    for row in reader:
        if row[3] == pnr:
            row[5] = "Cancelled"
        writer.writerow(row)
    print ("Your Ticket(s) have been cancelled")
    f.close()
    g.close()
    os.remove(r"/home/rohan/Python Files/Train.csv")
    os.rename(r"E:\Python Files\Temp.csv","E:\Python Files\Train.csv")
    h = input("Do you want to continue to Main Menu? (y/n)")
    if h == "Yy":
        railresmenu()
    else:
        print ("Have a great day!")
        
def PNRStatus():
    f = open(r"E:\Python Files\Train.csv","r")
    reader = csv.reader(f)
    pnr = input("Enter your PNR Number: ")
    for row in reader:
        if row[3] == pnr:
            print ("Your Ticket(s) is",row[5])
        else:
            continue
            
    f.close()
    h = input("Do you want to continue to Main Menu? (y/n)")
    if h == "Yy":
        railresmenu()
    else:
        print ("Have a great day!")

def Edit():
    f = open(r"E:\Python Files\Train.csv","r")
    g = open(r"E:\Python Files\Temp.csv","w",newline = "")
    reader = csv.reader(f)
    writer = csv.writer(g)
    pnr = input("Enter your PNR Number: ")
    for row in reader:
        while row[3] == pnr:
            p = input("What do you want to edit? \n 1.Name and Age \n 2.Travel Date ")
            if p == "1":
                name = input("Enter new name: ")
                age = input("Enter new age: ")
                na = [name,age]
                row[1] = na
                break
            elif p == "2":
                date = input("Enter new Travel date: ")
                row[0] = date
                break
            else:
                print ("Wrong Choice!!!")
                break
        writer.writerow(row)
    f.close()
    g.close()
    os.remove(r"E:\Python Files\Train.csv")
    os.rename(r"E:\Python Files\Temp.csv","E:\Python Files\Train.csv")
    print("The changes have been done!")
    print()
    railresmenu
    
def ShowTicket():
    f = open(r"E:\Python Files\Train.csv","r")
    reader = csv.reader(f)
    pnr = input("Enter your PNR Number: ")
    for row in reader:
        while row[3] == pnr:
            print ("\n Date of Journey: ",row[0],"\n",
                   "Name and Age: ",row[1],"\n",
                   "Your Car Tier: ",row[2],"\n",
                   "Your Ticket Fare: ",row[4],"\n",
                   "Your Ticker Status: ",row[5],"\n\n\n")
            break
    f.close()
    railresmenu()

railresmenu()
