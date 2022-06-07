def lcm(a,b,c):
    if a>b:
        a,b=b,a
    if b>c:
        b,c=c,b
    C=c
    while C%a!=0 or C%b!=0:
        C=C+c
    return C

a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
print('최소공배수는 ',lcm(a,b,c))
