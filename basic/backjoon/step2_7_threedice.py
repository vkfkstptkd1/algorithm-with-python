#처음에 틀림.
#틀린 이유 : a,b의 대소관계, a!=b!=c 는성립이 안됨. and로 해야함.
a,b,c=map(int,input().split())

if a == b and  b == c:
    print(a*1000+10000)
elif a!=b and a!=c and b!=c:
    if a>b:
        a,b=b,a
    if b>c:
        b,c=c,b
    print(c*100)
else:
    if a==b:
        print(1000+a*100)
    else:
        print(1000+c*100)

    