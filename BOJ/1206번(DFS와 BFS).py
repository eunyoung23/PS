# 내 풀이
from collections import deque

N,M,V = map(int,input().split())
graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
  a,b=map(int,input().split())
  graph[a][b]=1
  graph[b][a]=1

dfs_visited=[False]*N
def dfs(graph,v,dfs_visited):
  dfs_visited[v]=True
  print(v,end=' ')
  for w in range(len(graph[v])):
    if graph[v][w]==1 and dfs_visited[w] == False:
      dfs(graph,w,dfs_visited)

bfs_visited=[False]*N
def bfs(graph,start,bfs_visited):
  queue=deque([start])
  bfs_visited[start]=True
  while queue:
    v = queue.popleft()
    print(v,end=' ')
    for w in range(len(graph[v])):
      if graph[v][w]==1 and bfs_visited[w] == False:
        queue.append()


dfs(graph,1,dfs_visited)
bfs(graph,1,bfs_visited)



