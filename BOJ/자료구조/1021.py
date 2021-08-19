from collections import deque

N,M =map(int,input().split())
index = list(map(int,input().split()))
q=deque([i for i in range(1,N+1)])
count=0

for num in index:
    while 1:
        if q[0] == num:
            q.popleft()
            break
        #elif num<=q[N//2]:
        elif q.index(num) <= len(q)//2:
            q.append(q.popleft())
            count += 1
        else:
            q.appendleft(q.pop())
            count += 1

print(count)
