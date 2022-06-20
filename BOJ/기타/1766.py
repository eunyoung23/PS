#우선순위 큐 : 데이터 추가는 어떤 순서로 해도 상관이 없지만, 제거될 때는 가장 작은 값을 제거하는 독특한 특성을 지닌 자료구조임.
#Heapq : 최소힙의 구조
#import heapq
#hq=[]
#heapq.heappush(hq,4)
#heapq.heappush(hq,1)
#heapq.heappush(hq,3)
#heapq.heappush(hq,7)
#print(heapq.heappop(hq))-1
#print(heapq.heappop(hq))-3
#print(heapq.heappop(hq))-4
import heapq
import sys

input=sys.stdin.readline

answer=[]
N,M=map(int,input().split())
indegree=[0]*(N+1)
graph=[[]for _ in range(N+1)]
queue=[]

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    for i in range(1,N+1):
        if indegree[i]==0:
            heapq.heappush(queue,i)

    while queue:
        now=heapq.heappop(queue)
        answer.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                heapq.heappush(queue,i)


topology_sort()
print(" ".join(map(str,answer)))
