import sys

str=sys.stdin.readline().strip()
result=[0]*26

for s in str:
  result[ord(s)-ord('a')]+=1

for num in result:
  print(num,end=" ")
