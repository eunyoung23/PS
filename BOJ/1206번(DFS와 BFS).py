# 내 풀이
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




