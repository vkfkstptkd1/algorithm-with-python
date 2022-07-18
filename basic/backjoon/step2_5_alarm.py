#알람시계
#map: 리스트의 요소를 지정된 함수로 처리,
#     보통 여러 개의 데이터를 한 번에 다른 형태로 바꾸기 위해 사용.

h,m=map(int,input().split())#띄어쓰기 구분 정수형 저장.
if m<45:
    if h==0:
        h=23
    else:
        h-=1
    m=m-45+60
else:
        m-=45
print(f'{h} {m}')