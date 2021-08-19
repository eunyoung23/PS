from collections import deque

N,K = map(int,input().split())
data = deque([i for i in range(1,N+1)])
result = list()

while len(data)>0:
    for _ in range(K-1):
        data.append(data.popleft())
    result.append(data.popleft())

print("<", ', '.join(str(i) for i in result), ">",sep='')
