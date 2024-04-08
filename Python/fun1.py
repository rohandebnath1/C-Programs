def fun3(num1,num2):
    for x in range(num1,num2):
        if x%4==0:
            print(x,end='')
        fun3(10,20)
