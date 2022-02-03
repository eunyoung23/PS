# 풀이1
N,M = map(int,input().split(" "))
result = 0

for _ in range(N):
  arr = list(map(int,input().split(" ")))
  num = min(arr)
  result = max(num,result)

print(result)

# 풀이2(2중 반복문 구조를 이용하는 답안 예시)
N,M = map(int,input().split())
result = 0

for i in range(N):
  data = list(map(int,input().split()))
  min_value = 1001
  for a in data:
    min_value = min(min_value,a)
  result = max(min_value,result)

print(result) #최종답안 출력

