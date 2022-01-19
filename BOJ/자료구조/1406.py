from sys import stdin

stk1 = list(stdin.readline().strip())
stk2 = []
n = int(input())
for line in stdin:
  if line[0] == "L":
    if stk1:
      stk2.append(stk1.pop())
    else:
      continue
  elif line[0] == "D":
    if stk2:
      stk1.append(stk2.pop())
    else:
      continue
  elif line[0] == "B":
    if stk1:
      stk1.pop()
    else:
      continue
  elif line[0] == "P":
    stk1.append(line[2])

print("".join(stk1+list(reversed(stk2))))


# 문자열이나 리스트를 이용해서 insert메서드를 사용해서 글자를 삽입하는 방식으로 풀었지만 시간초과 판정이 남 -> 스택 2개로 커서 이동 
