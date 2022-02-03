#가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문에 그리디로 구현 가능함
N = 1260
money_types = [500,100,50,10]
count = 0

for money in money_types:
  count += N//money
  N %= money

print(count)

