def eratos(a,n):
    a[1]=0
    i=2
    while i<=(n/2):
        j=2
        while i*j<=n:
            a[i*j]=0
            j=j+1
        i=i+1
    return a

import random
a=[]
n=int(input('2 이상의 자연수 n:'))
for i in range (0,n+1):
    a.append(i)
print(a)
print(eratos(a,n))
