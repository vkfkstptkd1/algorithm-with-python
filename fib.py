def fib(n):
    a=1
    b=1
    c=0
    i=3
    while n<3:
        print('3이상 입력')
        n=int(input('n='))
    while i<=n:
        c=a+b
        a=b
        b=c
        i+=1
    return c
n=int(input('n='))
print('n번째 피보나치 수열은',fib(n),'입니다.')