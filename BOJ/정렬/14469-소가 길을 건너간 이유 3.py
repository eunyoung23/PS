'''
원래 배열 하나를 두고 이것에 따라 처리하려고 했으나 그럼 넘 복잡하고 시간초과가 날것이라고 판단함.
그냥 반복문을 돌려서 해결하기로 결정함
-> 첫번째 원소가 들어오면 소 도착시간 + 소 검문시간 더함.
'''
import sys

input=sys.stdin.readline

N=int(input())
result=0

arr=[]

for _ in range(N):
    arr.append(list(map(int,input().strip().split())))

arr.sort(key=lambda x:x[0])

result=-1
for i in range(len(arr)):
    if result<arr[i][0]:
        result=arr[i][0]+arr[i][1]
    else:
        result+=arr[i][1]

print(result)
