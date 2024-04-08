#find the mean of list of n integers

import statistics as st
val =[]
n = int(input("Enter the number of elements: "))

for i in range(0,n):
    val.append(input("Enter anything:"))
med = st.mode(val)
print ("Mode of the given list is:",med)