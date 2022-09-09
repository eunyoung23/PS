"""
row -> 2 -> 0,1
col -> 3 -> 0,1,2
m -> 3
idx -> 0, 1, 2, 3, 4, 5
-----------------
row -> 2 -> 0,1
col -> 2 -> 0,1
m -> 2
idx -> 0, 1, 2, 3
"""
import sys

input=sys.stdin.readline

N,M=map(int,input().strip().split())

graphs=[]

for _ in range(N):
    graphs.append(list(map(int,input().strip())))

ans=[]


for i in range(1<<N*M):
    total=0
    for row in range(N):
        rowsum=0
        for col in range(M):
            idx=row*M+col
            if i&(1<<idx)!=0:
                rowsum=rowsum*10+graphs[row][col]
            else:
                total+=rowsum
                rowsum=0
        total+=rowsum

    for col in range(M):
        colsum=0
        for row in range(N):
            idx=row*M+col
            if i&(1<<idx)==0:
                colsum=colsum*10+graphs[row][col]
            else:
                total+=colsum
                colsum=0
        total+=colsum
    ans.append(total)

print(max(ans))
