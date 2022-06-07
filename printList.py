def printList(a,n):
    i=0
    t=1
    c=1
    while i<n:
        print(a[i],end="")
        if t==c:
            print(end="\n")
            t+=1
            c=1
        else : c+=1
        i+=1
    return a
a=[]
n=int(input('n='))
for i in range(1,n+1):
    a.append(i)
print(a)
print(printList(a,n))