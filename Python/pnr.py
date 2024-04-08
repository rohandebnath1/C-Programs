import random
def pnr(n):
         range_start = 10**(n-1)
         range_end = (10**n)-1
         return random.randrange(range_start, range_end)
pnr(10)
