val = [17,23,18,19]
print ("The list is:",val)
while True:
    print("Main Menu")
    print("1.Insert")
    print("2.Delete")
    print("3.Exit")
    ch = int(input("Enter your choice 1/2/3:"))
    if ch==1:
        item = int(input("Enter item:"))
        pos = int(input("Insert at which posiiton:"))
        index = pos - 1
        val.insert(index,item)
        print("Success!List now is:",val)
    elif ch==2:
        print("DeletionMenu")
        print("1.Delete using value")
        print("2.Delete using index")
        print("3.Delete a sublist")
dch = int(input("Enter choice(1 or 2 or 3):"))
if dch == 1:
    item = int(input("Enter index of item to be deleted:"))
    val.remove(item)
    print("List now is:")
elif dch ==2:
    index = int(input("Enter index of item to be deleted:"))
    val.remove(item)
    print("List now is:",val)
elif dch == 3:
    l = int(input("Enter lower limit of list slice to be deleted:"))
    h = int(input("Enter upper limit of list slice to be deleted:"))
    del val[l:h]
    print ("List now is :",val)
else:
    print("valid choices are 1/2/3 only.")

    
