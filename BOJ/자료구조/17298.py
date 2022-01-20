#이중 for문을 사용했더니 시간 복잡도가 O(N제곱)으로 시간초과 판정이 남ㅠㅠ
N = int(input())
num = list(map(int,input().split(" ")))
stack = []
answer = [-1]*N

for i in range(N):
  while stack and num[stack[-1]] < num[i]:
    answer[stack.pop()] = num[i]
  stack.append(i)

print(*answer)
