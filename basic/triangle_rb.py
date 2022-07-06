#오른쪽 아래가 직각인 이등변 삼각형으로 * 출력

n=int(input("변의 길이: "))

#단일루프 : i와 n의 관계 사용
for i in range(1,n+1):
    print(' '*(n-i),end='')
    print('*'*i)

#다중루프 -- 꼭 하나만 들어갈 필요는 없잖아?
for i in range(1,n+1):
    for _ in range(0,n-i):
        print(' ',end='')
    for _ in range(0,i):
        print('*',end='')
    print()