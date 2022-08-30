#L인 경우 모두 L인 경우와 거리가 어느 정도인지 확인해서 최댓값을 탐색한다.
from collections import deque
import sys
import copy

input=sys.stdin.readline

N,M=map(int,input().split())

graphs=[]

for _ in range(N):
    graphs.append(list(input().strip()))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    max_num=0
    queue=deque()
    queue.append([x,y])
    test=[[0 for _ in range(M)]for _ in range(N)]
    visited=[[0 for _ in range(M)]for _ in range(N)]

    while len(queue)!=0:
        px,py= queue.popleft()
        visited[px][py]=1
        for i in range(4):
            moveX=px+dx[i]
            moveY=py+dy[i]

            if 0<=moveX<N and 0<=moveY<M and graphs[moveX][moveY]=='L' and visited[moveX][moveY]==0:
                visited[moveX][moveY]=1
                queue.append([moveX,moveY])
                test[moveX][moveY]=test[px][py]+1
                max_num=max(max_num,test[moveX][moveY])
    return max_num

resultList=[]

for i in range(N):
    for j in range(M):
        if graphs[i][j]=='L':
            resultList.append(bfs(i,j))

print(max(resultList))
