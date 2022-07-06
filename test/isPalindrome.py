def isPalindrome(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True

def change(s):
    a=''
    for i in range(len(s)):
        if s[i].isalpha():
            a+=s[i]
        a.lower()
    return a

s=input('s=')
a=change(s)
print(a)
if isPalindrome(a):
    print("회문입니다.")
else:
    print('회문이 아닙니다.')