import sys
import copy
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())

arr=[]
answer=[]

for _ in range(N):
    arr.append(list(map(int,input().split())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
    queue=deque()
    tmp_graph=copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j]==2:
                queue.append((i,j))

    while queue:
        numX,numY=queue.popleft()
        for i in range(4):
            nx=numX+dx[i]
            ny=numY+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if tmp_graph[nx][ny]==0:
                tmp_graph[nx][ny]=2
                queue.append((nx,ny))

    global answer
    count=0
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j]==0:
                count+=1
    answer.append(count)

def makeWall(cnt):
    if cnt==3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j]==0:
                arr[i][j]=1
                makeWall(cnt+1)
                arr[i][j]=0

makeWall(0)
print(max(answer))
