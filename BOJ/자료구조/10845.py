import sys

num = int(sys.stdin.readline())
line = []

for _ in range(num):
  cmd = sys.stdin.readline().split()
  
  if cmd[0] == "push":
    line.append(cmd[1])
  elif cmd[0] == "pop":
    if line: print(line.pop(0))
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
