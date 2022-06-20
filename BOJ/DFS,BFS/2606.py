import sys

input=sys.stdin.readline
n=int(input())
m=int(input())
graph=[[]for _ in range(n+1)]
visited=[False]*(n+1)
count=0

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(x):
    global count
    visited[x]=True
    count+=1

    for i in graph[x]:
        if visited[i]==False:
            dfs(i)
dfs(1)

print(count-1)
