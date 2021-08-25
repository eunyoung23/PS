from collections import deque

M,N,K = map(int,input().split())

dx=[-1,1,0,0]
dy=[0,0,1,-1]

board = [[0]*N for _ in range(M)]

for _ in range(K):
    left_x,left_y,right_x,right_y = map(int,input().split())
    for i in range(left_y,right_y):
        for j in range(left_x,right_x):
            board[i][j]=1


def bfs(i,j):
        queue = deque([])
        queue.append([i,j])
        board[i][j]=1
        cnt=1
        while queue:
            now = queue.popleft()
            x,y=now[0],now[1]
            for k in range(4):
                nY = y+dy[k]
                nX = x+dx[k]

            if 0<= nX < N and 0<= nY < M and board[nX][nY] ==0:
                queue.append([nX,nY])
                board[nX][nY]=1
                cnt+=1
        return cnt


area=0
cnts=[]
for i in range(M):
    for j in range(N):
        if board[i][j]==0:
            cnts.append(bfs(i,j))
            area+=1

print(area)
cnts.sort()
print(*cnts)
