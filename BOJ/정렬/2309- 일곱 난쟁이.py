import sys

input=sys.stdin.readline

arr=[]

for _ in range(9):
  arr.append(int(input()))

arr.sort()

for i in range(len(arr)-1):
  for j in range(i+1,len(arr)):
    if sum(arr)-arr[i]-arr[j]==100:
      n1=arr[i]
      n2=arr[j]
      arr.remove(n1)
      arr.remove(n2)
      break
    else:
      pass


for num in arr:
  print(num)
