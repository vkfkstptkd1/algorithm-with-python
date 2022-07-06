#10-99 사이 n개 난수 발생 후 13나오면 종료.
#for_else
import random

n=int(input("난수 개수 입력:"))

for i in range(n):
    r=random.randint(10,99)
    print(r,end=' ')
    if r==13:
        print("프로그램 종료")
        break #완전히 for문 종료.
else: #break가 실행되지 않을 경우에만 실행된다. for문 조건이 거짓일경우 사용.
    print('\n난수 생성 종료')

