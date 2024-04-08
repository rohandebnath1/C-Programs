#Display all prime numbers from 100 to 999

def Prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def Prime_range():
    for i in range(100,1000):
        if Prime(i):
            print(i, end=' ')

Prime_range()
