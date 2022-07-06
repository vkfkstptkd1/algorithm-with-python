def inputPoly():
    c=[]
    while True:
        b=[]
        s=0
        n=int(input("지수: "))
        a=int(input("계수: "))
        if n<0:
            break
        for i in range(len(c)):
            if n==c[i][0]:
                print("같은 지수 값을 가지는 원소가 있습니다.")
                s=1
                break
        if s==1:
            continue
        else:
            b.append(n)
            b.append(a)
            c.append(b)
    c.sort(reverse=True)
    print("다항식 리스트 :",c)
    return c

def printPoly(p):
    a=[]
    for i in range(len(p)):
        if p[i][0]==0:
            a.append(p[i][1])
        elif p[i][0]==1:
            a.append(p[i][1])
            a.append('x')
        else:
            a.append(p[i][1])
            a.append('x^')
            a.append(p[i][0])
        a.append(' + ')
    a.pop()
    for i in range(len(a)):
        print(a[i],end='')
    print('\n')

def evalPoly(p, x):
    s=0
    for i in range(len(p)):
        a=1
        if p[i][0]==0:
            s+=p[i][1]
            break
        for j in range(0,p[i][0]):
            a*=x
        a*=p[i][1]
        s+=a
    return s

def addPoly(a, b):
    c=[]
    m=len(a)
    n=len(b)
    i=0
    while i<m:
        d=[]
        j=0
        while j<n:
            if a[i][0]==b[j][0]:
                d.append(a[i][0])
                d.append(a[i][1]+b[j][1]) 
                c.append(d)

                a.remove(a[i])
                b.remove(b[j])
                n-=1
                m-=1
                i-=1
                j-=1
                break
            j+=1
        i+=1

    for j in range(len(b)):
        c.append(b[j])
    for j in range(len(a)):
        c.append(a[j])
        
    c.sort(reverse=True)
    return c

def multiplyPoly(a, b):
    c=[]
    for i in range(len(a)):
        for j in range(len(b)):
            d=[]
            d.append(a[i][0]+b[j][0])
            d.append(a[i][1]*b[j][1])
            c.append(d)
    
    c.sort(reverse=True)
    e=[]
    for i in range(len(c)-1):
        if c[i][0]==c[i+1][0]:
            s=0
            f=[]
            while c[i][0]!=c[i+1][0]:
                s+=c[i][1]+c[i+1][1]
                i+=1
            f.append(c[i][0])
            f.append(s)
            e.append(f)
            i-=1
        else:
            e.append(c[i]) 
    return e
    
m = 1
P = []
while m != 9:
    print('1. 다항식 입력')
    print('2. 다항식 출력')
    print('3. 다항식 계산')
    print('4. 다항식 덧셈')
    print('5. 다항식 곱셈')
    m = int(input('메뉴 선택 (종료시는 9) : '))
    if m == 1:
        print('다항식 입력 선택\n')
        P = inputPoly()
    elif m == 2:
        print('다항식 출력 선택\n')
        print("다항식 = ",end='')
        printPoly(P)
    elif m == 3:
        print('다항식 계산 선택\n')
        printPoly(P)
        X = int(input('X = '))
        result = evalPoly(P, X)
        print('계산 결과 : ', result)
    elif m == 4:
        print('다항식 덧셈 선택\n')
        A = inputPoly()
        B = inputPoly()
        print("다항식 A = ",end='')
        printPoly(A)
        print("다항식 B = ",end='')
        printPoly(B)
        C = addPoly(A, B)
        print("A + B = ", end='')
        printPoly(C)

    elif m == 5:
        print('다항식 곱셈 선택\n')
        A = inputPoly()
        B = inputPoly()
        print("다항식 A = ",end='')
        printPoly(A)
        print("다항식 B = ",end='')
        printPoly(B)
        C = multiplyPoly(A, B)
        print("A * B = ",end='')
        printPoly(C)
    else:
        if m != 9:
            print('메뉴 선택 오류\n')