import sys

input=sys.stdin.readline

N,M=map(int,input().split())

arr=list(map(int,input().split()))
arr.sort()
answer=[]
visited=[False for _ in range(N)]

def dfs():
    if len(answer)==M:
        print(" ".join(map(str,answer)))
    else:
        for i in range(len(arr)):
            if visited[i]==False:
                answer.append(arr[i])
                visited[i]=True
                dfs()
                answer.pop()
                visited[i]=False

dfs()