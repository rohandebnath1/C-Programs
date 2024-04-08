import mysql.connector as pymysql

con=pymysql.connect(host="localhost",user="root",passwd="12345",database="railways")
if con.is_connected():
    print("Successfully Connected :)")
cur=con.cursor()
pnr=1024

def railresmenu():
    print("Welcome to our rail reservation portal.")
    print("1.Train Detail")
    print("2.Reservation of Ticket")
    print("3.Cancellation of Ticket")
    print("4.Quit")
    n=int(input("Enter your choice:"))
    if n==1:
        traindetails()
    elif n==2:
        reservation()
    elif n==3:
        cancellation()
    elif n==4:
        Quit()
    else:
        print("Wrong Choice !")

def traindetails():
    src=input("Enter source:")
    dstnt=input("Enter destination:")
    sql1="select * from traindetails where source='{}' and destination='{}'".format(src,dstnt) 
    cur.execute(sql1)
    data=cur.fetchall()
    c=cur.rowcount
    print("Searching...")
    print("Number of available trains:",c)
    print("(Train_no., Train_name,  Source, Destination, AC1, Fair, AC2, Fair, Sleeper, Fair)")
    for r in data:
        print(r)
    railresmenu()
    

def reservation():
    global pnr
    pname=input("Enter passanger's name;")  
    src=input("Enter source:")
    dstnt=input("Enter destination:")
    sql1="select * from traindetails where source='{}' and destination='{}'".format(src,dstnt) 
    cur.execute(sql1)
    data=cur.fetchall()
    c=cur.rowcount
    print("Searching...")
    print("Number of available trains:",c)
    print("(Train_no., Train_name,  Source, Destination, AC1, Fair, AC2, Fair, Sleeper, Fair)")
    for r in data:
        print(r)
       
    t=int(input("Enter the train number of the train you wish to book:"))
    s=input("Enter the type of coach from the options [AC1,AC2,Sleeper]:")
    n=int(input("Enter number of seats you want to book:"))
    if s=='AC1'or'ac1':
        sql2="select fair_ac1*{} as 'Total Fair' from traindetails where train_no={}".format(n,t)
        cur.execute(sql2)
        data=cur.fetchall()
        for i in data:
            k=i[0]
            print("Total Fair is Rs ",k)
        sql3="update traindetails set ac1=ac1-{} where train_no={}".format(n,t)
        cur.execute(sql3)
        sql0="commit"
        cur.execute(sql0)
        sql4="select train_name from traindetails where train_no={}".format(t)
        cur.execute(sql4)
        data1=cur.fetchall()
        for j in data1:
            m=j[0]
        sql5="insert into passengerdetails values('{}',{},{},'{}','{}',{},{})".format(pname,pnr,t,m,s,n,k)
        cur.execute(sql5)
        sql6="commit"
        cur.execute(sql6)
    
    elif s=='AC2'or'ac2':
        sql2="select fair_ac2*{} as 'Total Fair' from traindetails where train_no={}".format(n,t)
        cur.execute(sql2)
        data=cur.fetchall()
        for i in data:
            k=i[0]
            print("Total Fair is Rs ",k)
        sql3="update traindetails set ac2=ac2-{} where train_no={}".format(n,t)
        cur.execute(sql3)
        sql0="commit"
        cur.execute(sql0)
        sql4="select train_name from traindetails where train_no={}".format(t)
        cur.execute(sql4)
        data1=cur.fetchall()
        for j in data1:
            m=j[0]
        sql5="insert into passengerdetails values('{}',{},{},'{}','{}',{},{})".format(pname,pnr,t,m,s,n,k)
        cur.execute(sql5)
        sql6="commit"
        cur.execute(sql6)
    
    elif s=='Sleeper'or 'sleeper':
        sql2="select fair_slp*{} as 'Total Fair' from traindetails where train_no={}".format(n,t)
        cur.execute(sql2)
        data=cur.fetchall()
        for i in data:
            k=i[0]
            print("Total Fair is Rs ",k)
        sql3="update traindetails set sleeper=sleeper-{} where train_no={}".format(n,t)
        cur.execute(sql3)
        sql0="commit"
        cur.execute(sql0)
        sql4="select train_name from traindetails where train_no={}".format(t)
        cur.execute(sql4)
        data1=cur.fetchall()
        for j in data1:
            m=j[0]
        sql5="insert into passengerdetails values('{}',{},{},'{}','{}',{},{})".format(pname,pnr,t,m,s,n,k)
        cur.execute(sql5)
        sql6="commit"
        cur.execute(sql6)

    
    print("Ticket Booked!")
    print("Your ticket details is shown below:")
    sql7="select * from passengerdetails where pnr={}".format(pnr)
    cur.execute(sql7)
    data2=cur.fetchall()
    for x in data2:
        print(x)
    pnr+=1    
    railresmenu()
    
def cancellation():
    global n
    global t
    p=int(input("Enter the pnr of your ticket:"))
    sql8="select * from passengerdetails where pnr={}".format(p)
    cur.execute(sql8)
    data3=cur.fetchall()
    for y in data3:
        l=y[4]
    if l=='AC1'or'ac1':
        sql9="update traindetails set ac1=ac1+{} where train_no={}".format(n,t)
        cur.execute(sql9)
        sql00="commit"
        cur.execute(sql00)
        
    elif l=='AC2'or'ac2':
        sql9="update traindetails set ac2=ac2+{} where train_no={}".format(n,t)
        cur.execute(sql9)
        sql00="commit"
        cur.execute(sql00)
        
    elif l=='Sleeper'or'sleeper':
        sql9="update traindetails set sleeper=sleeper+{} where train_no={}".format(n,t)
        cur.execute(sql9)
        sql00="commit"
        cur.execute(sql00)
        
    print("Ticket cancelled !")
    sql10="delete from passengerdetails where pnr={}".format(p)
    cur.execute(sql10)
    sql000="commit"
    cur.execute(sql000)
    
    railresmenu()
    
def Quit():
    print("Thanks for VIsiting!")
    
railresmenu()    
        
    
        

        

    
    