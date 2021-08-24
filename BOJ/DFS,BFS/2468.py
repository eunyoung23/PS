from collections import deque

n = int(input())
graph = []
max = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] > max:
            max=graph[i][j]

def bfs(xPos,yPos,value,visited):
    q=deque()
    q.append((xPos,yPos))
    visited[xPos][yPos]=1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <n and 0 <= ny <n:
                if graph[nx][ny] > value and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))

maximum = 0
for a in range(max): # 비가 안오는 경우인 0부터 max-1까지 조회(max는 모든 지역이 물에 잠기므로 안전영역이 0임 고려할 필요가 없음)
    visited = [[0]*n for _ in range(n)] # 매 높이마다 조회를 해야하므로 visited를 매번 정의
    ans=0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > a and visited[i][j] == 0 : # 비가 온것보다 높은 곳이고 방문하지 않은 경우 bfs호출
                bfs(i,j,a,visited)
                ans+=1
    if maximum<ans:
        maximum=ans
print(maximum)
