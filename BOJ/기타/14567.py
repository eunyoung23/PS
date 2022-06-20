#위상정렬 : 정렬 알고리즘의 일종으로 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할때 사용할 수 있는 알고리즘
#방향 그래프의 모든 노드를 "방향성에 거스르지 않도록 순서대로 나열하는 것" / 그래프상에서 선후 관계가 있다면, 위상 정렬을 수행하여 모든 선후 관계를 지키는 전체 순서를 계산할 수 있응.
#위상 정렬 알고리즘을 구현하기 전에, 먼저 진입차수(특정한 노드로 들어오는 간선의 개수)를 알아야 함.
from collections import deque
import sys

input=sys.stdin.readline

N,M=map(int,input().split())
indegree=[0]*(N+1)
graph=[[]for _ in range(N+1)]
result=[1]*(N+1)

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    q=deque()

    for i in range(1,N+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now=q.popleft()
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                result[i]=result[now]+1
                q.append(i)

    for i in range(1,N+1):
        print(result[i],end=" ")

topology_sort()
