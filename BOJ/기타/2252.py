from collections import deque
import sys

input=sys.stdin.readline

N,M=map(int,input().split())
graph=[[]for _ in range(N+1)]
indegree=[0]*(N+1)

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    q=deque()

    for i in range(1,N+1):
        if indegree[i]==0:
            q.append(i)
            print(i,end=" ")

    while q:
        now=q.popleft()
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
                print(i,end=" ")


topology_sort()
