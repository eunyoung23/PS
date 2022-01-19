# 그냥 input()으로 하면 시간초과 판정 나므로 sys.stdin.readline()함수 사용하기
import sys

num = int(sys.stdin.readline())
stack = list()

for _ in range(num):
  cmd = sys.stdin.readline().split()
  if cmd[0] == "push": #push인 경우
    stack.append(cmd[1])
  elif cmd[0] == "pop": #pop인 경우
    if len(stack)>0:
      num = stack.pop()
      print(num)
    else:
      print(-1)
  elif cmd[0] == "size": #size인 경우
    print(len(stack))
  elif cmd[0] == "empty": #empty인 경우
    if len(stack) == 0:
      print("1")
    else:
      print("0")
  else: #top인 경우
    if len(stack)>0:
      print(stack[-1])
    else:
      print("-1")
