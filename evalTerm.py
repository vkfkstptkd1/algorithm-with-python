def evalTerm(a,x,e):
    i=1
    while i<=e:
        a=a*x
        i+=1
    return a
print(evalTerm(4,2,3))