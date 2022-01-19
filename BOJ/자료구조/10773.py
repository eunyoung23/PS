num = int(input())
money = list()

for _ in range(num):
  x = int(input())
  if x == 0:
    money.pop()
  else:
    money.append(x)
  

print(sum(money))
