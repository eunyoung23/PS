import sys

input = sys.stdin.readline
d={}
for _ in range(int(input())):
    book = input()
    if book in d:
        d[book]+=1
    else:
        d[book]=1

m= max(d.values())
ans=''
for k,v in d.items():
    if v==m and (k<ans or ans==''):
        ans=k

print(ans)
