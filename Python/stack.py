
def PUSH(Q,w):
    Q.append(w)
    top = len(Q)-1
    

def POP(Q):
    if len(Q) == 0:
        print ("Stack Underflow")
    else:
        z = Q.pop()
        print (z,"is popped")

def DISPLAY(Q):
    if len(Q) == 0:
        print ("Stack is empty")
    else:
        Top = len(Q) - 1
        print ("Top Value is: ",Q[Top])
        print(Q[::-1])

stack = []
top = None
while True:
    p = int(input("Enter your choice: \n1.PUSH Element \n2.POP Element \n3.DISPLAY Stack"))
    if p == 1:
        w = input("Enter anything: ")
        PUSH(stack,w)
    elif p == 2:
        POP(stack)
    elif p == 3:
        DISPLAY(stack)
    else:
        print("Wrong Choice")
