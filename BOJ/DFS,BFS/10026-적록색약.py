import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

N=int(input())
graph=[]
visited=[[False]*N for _ in range(N)]
cnt1=0
cnt2=0

for _ in range(N):
    graph.append(list(input().rstrip()))

def dfs(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    visited[x][y]=True
    for i in range(4):
        nowx,nowy=x+dx[i],y+dy[i]
        if 0<=nowx<N and 0<=nowy<N and graph[x][y]==graph[nowx][nowy] and visited[nowx][nowy]==False:
            dfs(nowx,nowy)

for i in range(N):
    for j in range(N):
        if visited[i][j]==False:
            cnt1+=1
            dfs(i,j)

for i in range(N):
    for j in range(N):
        if graph[i][j]=='G':
            graph[i][j]='R'

visited=[[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j]==False:
            cnt2+=1
            dfs(i,j)

print(cnt1,cnt2)
