# 모의고사 문제 4

def emailSearch(t, p):
    tmp=0
    b=[]
    k=stringSearch(t[tmp:],p,0)
    a=""
    tmp += k+7
    while t[tmp]!='"':
        a+=t[tmp]
        tmp+=1
    b.append(a)

    k=stringSearch(t[tmp:],p,0)
    a=""
    tmp += k+7
    while t[tmp]!='"':
        a+=t[tmp]
        tmp+=1
    b.append(a)
    
    k=stringSearch(t[tmp:],p,0)
    a=""
    tmp += k+7
    while t[tmp]!='"':
        a+=t[tmp]
        tmp+=1
    b.append(a)    
    return b


def stringSearch(t, p, i):
    j = 0
    N = len(t)
    M = len(p)
    while i < N and j < M:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M:
        return i - M
    else:
        return i

fin = open('email.txt')
text = fin.read()
pattern = 'mailto:'
res = emailSearch(text, pattern)
for i in range(len(res)):
    print(res[i])
