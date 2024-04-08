time = {}
n = int(input("Enter thr number of times to enter:"))
for i in range (n):
    hr = int(input("Enter the hour: "))
    mi = int(input("Enter the minute: "))
    sec = int(input("Enter the second: "))
    d = dict(zip(("Hr","Min","Sec")(hr,mi,sec)))
    time.append(d)
print (time)






