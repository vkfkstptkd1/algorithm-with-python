def makenum(s):
    a=0
    for i in range(len(s)):
        a*=10
        a+= ord(s[i])-48
    return a
s=input('s=')
print('결과:',makenum(s))