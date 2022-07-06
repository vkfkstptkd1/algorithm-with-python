#모의고사 문제 1

def count2DList(a, n, k):

    b=[]

    for i in range(len(a)):

        c=0

        for j in range(len(a[i])):

            if a[i][j]==k:

                c+=1

        b.append(c)

    return b

 

def makeList(n):

    a = []

    for i in range(n):

        b = []

        r = random.randint(1, n)

        for j in range(r):

            b.append(random.randint(1, n))

        a.append(b)            

    return a            

    

import random

N = int(input('N = '))

while N < 3:

    print('N는 3 이상이어야 합니다.')

    N = int(input('N = '))

K = int(input('K = '))

while K < 1 or K > N:

    print('K는 1부터 %d 이하여야 합니다.'%N)

    K = int(input('K = '))

A = makeList(N)        

print('A =', A)

print()

B = count2DList(A, N, K)

print('B =', B)