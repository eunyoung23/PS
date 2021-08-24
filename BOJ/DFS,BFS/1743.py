import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())

board = [[0]*M for _ in range(N)]
visit = [[0]*M for _ in range(N)]

for _ in range(K):
    a,b = map(int,input().split())
    board[a-1][b-1]=1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = []
def bfs(x,y):
    global v
    queue.append([x,y])
    visit[x][y]=1
    v+=1

    while queue:
        x,y = queue[0][0],queue[0][1]
        del queue[0]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<M and visit[nx][ny]==0 and board[nx][ny]==1:
                queue.append([nx,ny])
                visit[nx][ny]=1
                v+=1


result = 0 #총 쓰레기 개수
v = 0 # 쓰레기 개수

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            bfs(i,j)
            result = max(result,v)

print(result)
