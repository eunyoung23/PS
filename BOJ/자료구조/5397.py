from sys import stdin
for _ in range(int(stdin.readline())):
  typing = stdin.readline().strip()
  leftList, rightList = [],[]
  for type in typing:
    if type == "<":
      if leftList:
        rightList.append(leftList.pop())
      else:
        pass
    elif type == ">":
      if rightList:
        leftList.append(rightList.pop())
      else:
        pass
    elif type == "-":
      if leftList:
        leftList.pop()
      else:
        pass
    else:
      leftList.append(type)
  print("".join(leftList+list(reversed(rightList))))
