def isPrime(a):
    i=2
    while i<=(a/2):
        if a%i==0:
            return False
        i+=1
    return True
a=int(input('a='))
if isPrime(a)==True:
    print(a,'는(은) 소수.')
else:
    print(a,'는 소수가 아닌 자연수.')
    