#0<=a<=23
#0<=b<=59
#0<=c<=1000 요리하는 데 필요한 시간.
#처음에 a가 23이상이 될 경우 예외처리 안함.

a,b=map(int,input().split())
c=int(input())
if b+c<60:
    b+=c
else:
    a+=(b+c)//60
    if a>=24:
        a=a%24
    b=(b+c)%60

print(f'{a} {b}')