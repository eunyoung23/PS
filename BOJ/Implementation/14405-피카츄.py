import sys

input=sys.stdin.readline

S=input().strip()
arr=[]

for str in ["pi","ka","chu"]:
    if str in S:
        S=S.replace(str,"*")

flag=True
for i in S:
    if i=="*":
        pass
    else:
        flag=False

if flag==False:
    print("NO")
else:
    print("YES")
