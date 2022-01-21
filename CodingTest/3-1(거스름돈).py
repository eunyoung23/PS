N = 1260
money_types = [500,100,50,10]
count = 0

for money in money_types:
  count += N//money
  N %= money

print(count)
