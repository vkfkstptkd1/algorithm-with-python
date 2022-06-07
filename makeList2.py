def makeList(s):
    a, i, n=[],0,len(s)
    while i<n:
        tmp = ''
        while i<n and ord(s[i]) != 32:
            tmp += s[i]
            i+=1
        a.append(tmp)
        i +=1
    return a
s= input('문자열:')
print('결과:',makeList(s))
