n=int(input("몇 개를 입력할건가요:"))
m=int(input("몇 개마다 줄바꿈할건가요:"))

for _ in range(n//m):
	print("*"*m)
rest = n%m
if rest:
	print("*"*rest)
# 어떻게 이런 생각을 할까? 내 머리를 반성하자