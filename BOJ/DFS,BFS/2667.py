N = int(input())

board = [[0]*N for _ in range(N)]
visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        board[i-1][j-1]=int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = []
def bfs(x,y):
    global v
    queue.append([x,y])
    visited[x][y]=1
    v+=1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and board[nx][ny] == 1:
            queue.append([nx, ny])
            visited[nx][ny] = 1
            v += 1


for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            bfs(i,j)
            print(v)
