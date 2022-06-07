#\ -*- coding: utf-8 -*- 
def countList(a, n, k):
    b=[]
    for i in range (0,k):
        s=0
        for j in range (0,n):
            if a[j]==i+1:
                s+=1
        b.append(s)
    return b

import random
K = int(input('K = '))
while K < 3:
 print('K는 3 이상이어야 합니다.')
 K = int(input('K = '))
N = int(input('N = '))
A = []
for i in range(N):
 A.append(random.randint(1, K))
print('A =', A)
print()
B = countList(A, N, K)
print('B =', B)
print()
for i in range(K):
 print(i+1, '의 개수 : ', B[i])