#product items dictionary 

product = {}
n = int(input("Enter the number of products: "))
for i in range (n):
    p = {}
    p['Pid'] = int(input("Enter product id: "))
    p['Pname'] = input("Enter product name: ")
    p['Mfg'] = input("Enter product mfg in dd/mm/yyyy: ")
    p['price'] = int(input("Enter the product price:"))
    p['Qty'] = int(input("Enter product quantity: "))
    product[i] = p
print(product)

#Task 1 : Display the details if all products which manufactured in year 2020
p = {0: {'Pid': 32, 'Pname': 'cfg', 'Mfg': '10/20/2020', 'price': 54, 'Qty': 465}, 1: {'Pid': 45, 'Pname': '654', 'Mfg': '10/2/2022', 'price': 64, 'Qty': 5}}

def Task1(p):
    for i in p.keys():
        if p[i]['Mfg'][6:] == '2020':
            print ("Product details manufactured in 2020:",product[i])
Task1(p)

#Task 2 : Display the product which name starts with H and price > 300

def Task2(p):
    for i in p.keys():
        if p[i]['Pname'][0].upper == 'H':
            if p[i]['price'] > 300:
                print ("Product details are:", product[i])
Task2(p)

#Task 3 : Display details of the products on basis of the id given by user

def Task3(p,ID):
    for i in range (I, len(p)):
        if p[i]['Pid'] == ID:
            print ("PID",p[i]['Pid'])
            print ("Pname",p[i]['Pname'])
            return
    print ("Product ID doesn't exist")
ID = int(input("Enter the ID to be searched: "))
Task3()
            
            
            
    
