def perfect(a):
    s=0
    i=1
    while i<=(a/2):
        if a%i==0:
            s+=i
        i+=1
    if s==a:
        return 1
    elif s>a:
        return 2
    return 3

a=int(input('a='))
if perfect(a)==1:
    print('완전수 입니다.')
elif perfect(a)==2:
    print('과잉수 입니다.')
else:
    print('부족수 입니다.')
