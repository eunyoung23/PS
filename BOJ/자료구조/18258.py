import sys
from collections import deque

num = int(sys.stdin.readline())
line = deque()

for _ in range(num):
  cmd = sys.stdin.readline().split()
  
  if cmd[0] == "push":
    line.append(cmd[1])
  elif cmd[0] == "pop":
    if line: print(line.popleft())
    else: print(-1)
  elif cmd[0] == "size":
    print(len(line))
  elif cmd[0] == "empty":
    if line: print(0)
    else: print(1)
  elif cmd[0] == "front":
    if line: print(line[0])
    else: print(-1)
  else:
    if line: print(line[-1])
    else: print(-1)
      
# 그냥 list를 써서 pop부분을 line.pop(0)했더니 시간초과가 남 -> deque를 써서 pop하는 부분을 line.popleft()로 변경하니 통과함
