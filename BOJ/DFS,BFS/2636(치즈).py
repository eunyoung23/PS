#1.DFS를 이용해서 푼다.
#2.공기인 부분을 큐에 넣어주고
#3.시간과 치즈의 개수를 어떻게 구할것인가
from collections import deque
import sys

input=sys.stdin.readline

A,B=map(int,input().split())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
cheese=[]
time=0

graphs=[]

for _ in range(A):
    graphs.append(list(map(int,input().split())))

def find_air():
    visited=[[False]*B for _ in range(A)]

    q=deque()
    q.append([0,0])
    visited[0][0]=True
    cnt=0

    while len(q)!=0:
        px,py=q.popleft()
        for i in range(4):
            pointx=px+dx[i]
            pointy=py+dy[i]
            if 0<=pointx<A and 0<=pointy<B and visited[pointx][pointy]==False: #여기 순서 조심하기! 바꾸어주면 런타임 에러가 남.
                if graphs[pointx][pointy]==0:
                    visited[pointx][pointy] = True
                    q.append([pointx,pointy])
                elif graphs[pointx][pointy]==1:
                    graphs[pointx][pointy]=0
                    cnt+=1
                    visited[pointx][pointy]=True

    cheese.append(cnt)
    return cnt

time=0
while True:
    time+=1
    cnt=find_air()
    if cnt==0:
        break

print(time-1)
print(cheese[-2])
