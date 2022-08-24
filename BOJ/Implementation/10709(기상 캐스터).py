import sys

input=sys.stdin.readline

H,W=map(int,input().split())
graphs=[]
index=[]
answer=[[-1 for _ in range(W)]for _ in range(H)]

for _ in range(H):
    graphs.append(list(input().rstrip()))

for i in range(H):
    for j in range(W):
        if graphs[i][j]=='c':
            answer[i][j]=0
            index.append([i,j])

for x,y in index:
    num=0
    while y<W-1:
        num += 1
        y+=1
        if answer[x][y]==0:
            break
        answer[x][y]=num

for i in answer:
    for j in i:
        print(j,end=" ")
    print("")
