#2자리 양수 (10-99) 입력받기
#드모르간 법칙

print('2자리 양수 입력하세용')

while True:
    no = int(input("값 입력:"))
    if no>=10 and no<=99:
    # = if not (no<10 or no>99) -- 드모르간
    # = if (10 <= no <= 99)  -- and 결합
        break

print(f'입력받은 양수는 {no} 입니다.')