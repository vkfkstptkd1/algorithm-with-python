#모의고사 문제 2

def makeNum(s):
    a=0
    b=[]
    for i in range(len(s)):
        if 97<=ord[s] and ord[s]<=122:
            i+=1
        a*=10
        a+= ord(s[i])-48
        b.append(a)
    return b

def isNum(s):
    for i in range(len(s)):
        if ord(s[i]) < 48 or (ord(s[i]) > 57 and ord(s[i]) < 97) or ord(s[i]) > 122:
            return False
    return True        
    
S = input('S = ')
while not isNum(S):
    print('숫자와 영문소문자만 입력 가능합니다.')
    print()
    S = input('S = ')
A = makeNum(S)
print('A = ', A)