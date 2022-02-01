import sys
from collections import deque

N,M = map(int,input().split(" "))
dx = [1,-1,0,0]
dy = [0,0,1,-1]

board = [[0]*(N) for _ in range(N)]
board[1][1]=2
switchs = [[] for _ in range(N)]for _ in range(N) ]

for _ in range(M):
  x,y,a,b = map(int,input().split(" "))
  switchs[x][y].append([a,b])

def bfs(x,y):
  for i in range(4):
    xx = x+dx[i]
    yy = y+dy[i]
