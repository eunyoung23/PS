import sys

input=sys.stdin.readline

def dfs(num,arr):
    arr[num]=-2
    for i in range(len(arr)):
        if num==arr[i]:
            dfs(i,arr)

N=int(input())
arr=list(map(int,input().split()))
K=int(input())
count=0

dfs(K,arr)

for i in range(len(arr)):
    if arr[i]!=-2 and i not in arr:
        count+=1

print(count)
