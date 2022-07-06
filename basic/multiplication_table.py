# 다중루프

#구구단 표 출력
print('-'*27)
for i in range(1,10):
    for j in range(1,10):
        print(f'{i*j:3}', end = '')#:3 -> 3자리로 가지런하게 출력
    print()

print('-'*27)