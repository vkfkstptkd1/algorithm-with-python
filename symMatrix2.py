# 모의고사 문제 3

def symMatrix(a, m):
    i=0 #행
    b=[]
    c=[]
    for i in range(m-1):
        j = i+1 #열
        while j!=m:
            if a[i][j]==a[j][i]:
                b.append([i+1,j+1])
            else:
                c.append([i+1,j+1])
            j+=1
    return (b,c) #튜플 자료형


def makeMatrix(m):
    a = []
    for i in range(m):
        b = []
        for j in range(m):
            if i == j:
                b.append(0)
            else:
                b.append(random.randint(0, 1))
        a.append(b)
    return a

def printMatix(a, m):
    for i in range(m):
        for j in range(m):
            print(a[i][j], end=' ')
        print()            

import random
M = int(input('M = '))
while M < 3:
    print('M은 3 이상이어야 합니다.')
    M = int(input('M = '))
A = makeMatrix(M)
print()
printMatix(A, M)
print()
res = symMatrix(A, M)
print()
print('대칭인 원소의 주소 :', res[0])
print('대칭이 아닌 원소의 주소 :', res[1])