#치킨 가게를 M개를 뽑아내는 것을 코드로 구현해야하는데 어떻게 할지 -> 조합을 이용해서 4중 반복문으로 해결하려고 했으나 실
import sys
from itertools import combinations

input=sys.stdin.readline

N,M=map(int,input().split())
graph=[]
chicken=[]
house=[]
store=[]
result=99999

for _ in range(N):
    graph.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j]==2:
            chicken.append([i,j])
        if graph[i][j]==1:
            house.append([i,j])

for chi in combinations(chicken,M):
    temp=0
    for h in house:
        chi_len=999
        for j in range(M):
            chi_len=min(chi_len,abs(h[0]-chi[j][0])+abs(h[1]-chi[j][1]))
        temp+=chi_len
    result=min(result,temp)

print(result)
