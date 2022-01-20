N = int(input())
num = list(map(int,input().split(" ")))
answer = list()

for i in range(1,N):
  stack1 = num[:i]
  stack2 = num[i:]
  if stack1.pop() <:
