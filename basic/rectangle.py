# 가로 세로 길이가 정수이고 넓이가 area인 직사각형의 변의 길이 나열
area=int(input("넓이 입력: "))

for i in range(1,area+1):
    if i*i>area: break #최대 넓이 초과시 종료.
    if area%i: continue #나머지가 있으면 for의 다음 반복으로 진행. 
    print(f'{i} x {area // i}') #핵심.. 약수만 출력. 짧은변 * 긴변