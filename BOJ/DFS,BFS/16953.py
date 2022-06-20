from collections import deque
import sys

input=sys.stdin.readline

start,end=map(int,input().split())
result=-1

def bfs():
    global start
    global end
    global result
    arr=deque()
    arr.append([start,1])
    
    while not len(arr)==0:
        num,cnt=arr.popleft()

        if num==end:
            result=cnt
            break

        myVal=num*2
        if myVal<=end:
            arr.append([myVal,cnt+1])

        myVal=int(str(num)+"1")
        if  myVal<=end:
            arr.append([myVal, cnt+1])

bfs()
print(result)
