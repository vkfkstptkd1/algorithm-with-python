def symMatrix(a,m):
    i=0
    s=0
    while i<m:
        j=m-1
        while j != i :
            if a[j][i]==1 and a[i][j]==1:
                s+=1
            j-=1
        i+=1
    return s
def makeMatrix(m):
    a=[]
    for i in range(m):
        b=[]
        for j in range(m):
            if i==j:
                b.append(0)
            else:
                b.append(random.randint(0,1))
        a.append(b)
    return a
def printMatrix(a,m):
    for i in range(m):
        for j in range(m):
            print(a[i][j],end=' ')
        print()
import random
M = int(input('M='))
A = makeMatrix(M)
print()
printMatrix(A,M)
print()
res=symMatrix(A,M)
print('합 : ',res)