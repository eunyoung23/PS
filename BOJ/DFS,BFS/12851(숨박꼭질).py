#3,3인 경우도 생각하기!!
from collections import deque
import sys

input=sys.stdin.readline

N,K=map(int,input().split())

CHECK_MAX=100001

check=[-1 for _ in range(CHECK_MAX)]

queue=deque()
queue.append(N)
check[N]=0
cnt=0

while len(queue)!=0:
    point=queue.popleft()

    if point==K:
        cnt+=1

    for i in [point-1,point+1,point*2]:
        if 0<=i<100001:
            if check[i]==-1 or check[i]>=check[point]+1:
                check[i]=check[point]+1
                queue.append(i)


print(check[K])
print(cnt)
