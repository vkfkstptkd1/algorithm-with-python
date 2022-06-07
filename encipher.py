def encipher(p,k):
    a = ord(p)
    C=''
    if a==32:
        a=96
        a+=k
    if a>122:
        a-=27
    if a==96:
        a=32
    for i in range(len(p)):
        C+=encipher()
        
P = input('평문 입력 : ')
K = int(input('K값 입력(1~26) :'))
while K<1 or K>26:
    K=int(input('K값 입력(1~26): '))
C = encipher(P,K)
print('암호문 출력 : [', end='')
print(C,end='')
print(']')