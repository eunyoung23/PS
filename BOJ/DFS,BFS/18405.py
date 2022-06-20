from collections import deque
import sys

input=sys.stdin.readline

N,K=map(int,input().split())
graph=[list(map(int,input().split()))for _ in range(N)]
virus=[]
cnt=0
S,X,Y=map(int,input().split())
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(N):
    for j in range(N):
        if graph[i][j]!=0:
            virus.append((graph[i][j],i,j))

virus.sort()
q=deque(virus)
while q:
    if cnt==S:
        break
    for _ in range(len(q)):
        pos = q.popleft()
        for i in range(4):
            numX = pos[1] + dx[i]
            numY = pos[2] + dy[i]
            if numX >= 0 and numX <= N - 1 and numY >= 0 and numY <= N - 1:
                if graph[numX][numY]==0:
                    graph[numX][numY] = pos[0]
                    q.append([pos[0], numX, numY])
    cnt+=1

print(graph[X-1][Y-1])
