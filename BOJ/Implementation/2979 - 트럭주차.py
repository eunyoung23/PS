#겹치는 구간을 어떻게 구할것인가
import sys

input=sys.stdin.readline

arr=[0]*100
A,B,C=map(int,input().split())

cal1=0
cal2=0
cal3=0

for _ in range(3):
  begin,end=map(int,input().split())
  for point in range(begin,end):
    arr[point]+=1

for num in arr:
  if num==3:
    cal3+=1
  elif num==2:
    cal2+=1
  elif num==1:
    cal1+=1

print(cal3*C*3+cal2*2*B+cal1*1*A)
