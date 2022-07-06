#직각 이등변 삼각형 출력
# ver 1 : 단일 루프와 곱셈
# ver 2 : 다중 루프
n=int(input("변의 길이:"))

#ver 1
for i in range(1,n+1):
    print('*'*i)

#ver 2
for i in range(1,n+1):
    for j in range(i):
        print('*',end='')
    print()


