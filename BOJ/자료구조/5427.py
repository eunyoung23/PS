from collections import deque
import sys

input = sys.stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]
q=deque()

def dfs(x,y):
    q.append([x,y])
    c[x][y]=1
    while q:
        qlen = len(q)
        while qlen:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<h and 0<=ny<w:
                    if a[nx][ny] =='.' and c[nx][ny] == 0:
                        c[nx][ny] = c[x][y]+1
                        q.append([nx,ny])
                    elif nx<0 or ny<0 or nx>=h or ny>=w:
                        print(c[x][y])
                        return
