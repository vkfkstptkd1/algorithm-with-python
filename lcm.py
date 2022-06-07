def lcm(a,b):
    if a>b:
        a,b=b,a
    B=b
    while B % a !=0:
        B=B+b
    return B

a=int(input('a='))
b=int(input('b='))
print('a,b의 최소공배수는',lcm(a,b))
