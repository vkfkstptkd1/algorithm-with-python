def sum(n):
    sum=0
    i=1
    while i<=n:
        sum+=i
        i+=1
    return sum
n=int(input("n="))
result=sum(n)

print("합:",result)
