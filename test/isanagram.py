def isanagram(a,b):
    if len(a)!=len(b):
        return False
    al,bl=list(a),list(b)
    al.sort()
    bl.sort()
    if al==bl:
        return True
    else:
        return False

def change(s):
   tmp=''
   for i in range(len(s)):
       if s[i].isalpha():
           tmp+=s[i]
   return tmp.lower()

a=input('a-')
b=input('b-')

A=change(a)
B=change(b)
if isanagram(A,B):
    print("어구전철")
else:
    print("ㅌ")