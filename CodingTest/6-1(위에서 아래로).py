# 내 풀이
N = int(input())
arr = []
for _ in range(N):
  arr.append(int(input()))

arr.sort(reverse=True)

for i in range(N):
  print(arr[i],end=' ')
  
#풀이1
N = int(input())
arr = []
for _ in range(N):
  arr.append(int(input()))

arr = sorted(arr,reverse=True)

for i in arr:
  print(i,end=' ')

  
