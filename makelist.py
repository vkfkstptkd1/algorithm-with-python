def makeList(n):
	a=[]
	b=[]
	for i in range (0,n):
		b.append([])
		for j in range (0,i+1):
			b[i].append(j+1)
		a.append(b[i])
	return a
N= int(input('n='))
print('A= ', makeList(N))

