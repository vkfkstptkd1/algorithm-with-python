import random
def symMatrix(a,m):
    s=0
    for i in range(0,m):
        j=i+1
        while j < m :
            if a[i][j]==a[j][i] and a[i][j]==1:
                s+=1
            j+=1
    return s
def makeMatrix(m):
    b=[]
    for i in range(0,m):
        a=[]
        for j in range(0,m):
            if i==j:
                a.append(0)
            else:
                a.append(random.randint(0,1))
        b.append(a)
    return b
def printMatrix(a):
    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            print(a[i][j],end=' ')
        print()

m=int(input('m='))
a=makeMatrix(m)
printMatrix(a)
print("원소 개수",symMatrix(a,m))
            

