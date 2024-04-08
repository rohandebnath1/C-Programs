d = {}
n = int(input("Enter the number of products: "))
w = []
for i in range(n):
    p_id = int(input("Enter the product id: "))
    name = input("Enter the product name: ")
    w = [p_id,name]
    d[i] = w
print (d)

