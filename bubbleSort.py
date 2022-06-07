def bubbleSort(a,n):
    i=n-1
    while i>0:
        for j in range(0,i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
        i=i-1
    return a

import random
a=[]
n=int(input('n='))
for i in range (0,n):
    a.append(random.randint(0,n))
print(a)
print('정렬 후',bubbleSort(a,n))