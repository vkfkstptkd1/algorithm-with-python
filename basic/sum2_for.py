def sum2(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
n=int(input("n="))
print("합:",sum2(n))