# 내 풀이
import sys
sys.setrecursionlimit(10**9)

input=sys.stdin.readline

T=int(input())
dx=[1,-1,0,0]
dy=[0,0,1,-1]

resultList=[]

def make_graph(M,N,K):
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        num1, num2 = map(int, input().split())
        graph[num2][num1] = 1
    return graph

def dfs(x,y):
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False

    if graph[x][y]==1:
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    else:
        return False


for _ in range(T):
    result=0
    M,N,K=map(int,input().split())
    graph=make_graph(M,N,K)
    cnt=0
    for i in range(N):
        for j in range(M):
             if dfs(i,j)==True:
                    cnt+=1
    resultList.append(cnt)

for i in range(len(resultList)):
    print(resultList[i])
