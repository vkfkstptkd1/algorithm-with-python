def stringSearch(t,p):
    i,j,n,m=0,0,len(t),len(p)
    while i<n and j<m:
        if t[i] != p[j]:
            i-=j
            j= -1
        i +=1
        j +=1
    if j == m :
        return i-m
    else:
        return i

text = 'A lover asked his beloved, Do you love yourself more than me?'
print('텍스트 :', text)
pattern = input('패턴 입력 : ')
K = stringSearch(text, pattern)
if K < len(text): print('패턴을 처음 발견한 위치 :', K)
else: print('패턴을 발견하지 못함.') 
