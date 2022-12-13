'''
import sys

input=sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=int(input())
a=[list(map(int,input().split()))for _ in range(N)]
a.insert(0,[0]*n)
a.append([0]*n)
for x in a:
    x.insert(0,0)
    x.append(0)
cnt=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)
'''
import sys

input=sys.stdin.readline

N=int(input())

arr=[[0 for _ in range(N+2)]for _ in range(N+2)]

tmp=[]
result=0

for _ in range(N):
    tmp.append(list(map(int,input().split())))

for i in range(1,N+1):
    for j in range(1,N+1):
        arr[i][j]=tmp[i-1][j-1]

for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j]>arr[i-1][j] and arr[i][j]>arr[i][j-1] and arr[i][j]>arr[i][j+1] and arr[i][j]>arr[i+1][j]:
            result+=1

print(result)
