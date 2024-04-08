#Data Strutures 


def push(s,n):
    s.append(n)
    Top=len(s)-1
def pop(s):
    if s==[]:
        print("Stack is Empty!")
    else:
        q=s.pop()
        print(q," is Poped ")
        Top=len(s)-1
def display(s):
    if s==[]:
        print("Stack is Empty")
    else:
        Top=len(s)-1
        print("Top Value is: ",s[Top])
        for i in range (Top,-1,-1):
            print(s[i],end=",")

#main
stk=[]
Top=None
while True:
    ch=int(input("\n 0->Exit \n 1->PUSH() \n 2->POP() \n 3->DISPLAY() \nEnter the option: "))
    if ch==1:
        x=int(input("Enter the Number: "))
        push(stk,x)
    elif ch==2:
        pop(stk)
    elif ch==3:
        display(stk)
    elif ch==0:
        break
