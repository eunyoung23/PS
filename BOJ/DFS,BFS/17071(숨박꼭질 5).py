from collections import deque
import sys

input=sys.stdin.readline

N,K=map(int,input().split())

CHECK_MAX=100001

check=[-1 for _ in range(CHECK_MAX)]
move=[0 for _ in range(CHECK_MAX)]

queue=deque()
queue.append(N)
check[N]=0
cnt=0

def path(x):
    result=[]
    temp=x
    for _ in range(check[x]+1):
        result.append(temp)
        temp=move[temp]
    print(' '.join(map(str, result[::-1])))


while len(queue)!=0:
    point=queue.popleft()

    if point==K:
        print(check[point])
        path(K)
        break

    for i in [point-1,point+1,point*2]:
        if 0<=i<100001:
            if check[i]==-1 or check[i]>=check[point]+1:
                check[i]=check[point]+1
                move[i]=point
                queue.append(i)
