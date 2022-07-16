from typing import Any,Sequence
def search(x:Sequence,key:Any)->Any:
    for z in range(len(x)):
        if x[z]==key:
            return z
    return -1

print("실수를 검색합니다.")
print("주의: 'End'를 입력하면 종료합니다.")

x=[]
i=0
while True:
    n=input(f"x[{i}]=")
    if n=='End':
        break
    x.append(n)
    i+=1
    
key=input("찾는 값을 입력해주세요: ")
idx=search(x,key)

if idx:
    print(f'찾는 값은 x[{idx}]입니다.')
else:
    print("찾는 값이 없습니다.")

