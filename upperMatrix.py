import random
from re import M
def uppermatrix(a,m):
    s=0
    for i in range (0,m):
        for j in range(0,m):
            if i<j:
                s+=a[i][j]
    return s

def makeMatrix(m):
    b=[]
    for i in range(0,m):
        a=[]
        for j in range(0,m):
            if i==j:
                a.append(0)
            else:
                a.append(random.randint(0,3))
        b.append(a)
    return b

m=int(input('m='))
a=makeMatrix(m)
print(a)
print('합:',uppermatrix(a,m))

