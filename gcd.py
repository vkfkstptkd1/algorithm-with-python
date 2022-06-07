def gcd(a,b):
    if a>b:
        a,b=b,a
    for i in range(1,a+1):
        if (a%i==0) and (b%i==0):
            c=i
    return c

a=int(input('a='))
b=int(input('b='))

print('a와 b의 최대공약수는:',gcd(a,b))