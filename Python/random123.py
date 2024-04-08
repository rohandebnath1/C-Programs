'''import random
List = ['Delhi', 'Mumbai','Chennai','Kolkata']
for y in range(4):
    x = random.randint(1,3)
    print(List[x],end='#')
'''    
import random
AR = [20,30,40,50,60,70]
FROM = random.randint(1,3)
TO = random.randint(2,4)
for K in range (FROM,TO+1):
    print(AR[K],end='#')
