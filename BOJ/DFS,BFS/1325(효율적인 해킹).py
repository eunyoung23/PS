import sys
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())

graphs=[[] for _ in range(N+1)]

def bfs(start):
    cnt=1
    queue=deque([start])
    visited=[False for _ in range(N+1)]
    visited[start]=True

    while queue:
        cur=queue.popleft()

        for nx in graphs[cur]:
            if not visited[nx]:
                visited[nx]=True
                cnt+=1
                queue.append(nx)

    return cnt

for _ in range(M):
    num1,num2=map(int,input().split())
    graphs[num2].append(num1)

maxCnt=1
ans=[]

for i in range(1,N+1):
    cnt=bfs(i)
    if cnt>maxCnt:
        maxCnt=cnt
        ans.clear()
        ans.append(i)
    elif cnt==maxCnt:
        ans.append(i)


print(*ans)
