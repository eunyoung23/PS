from collections import deque

num = int(input())
card = deque()

for i in range(num):
  card.append(i+1)

while len(card)>1:
  card.popleft()
  card.append(card.popleft())

#print(card.popleft())이거나
print(card[0])
