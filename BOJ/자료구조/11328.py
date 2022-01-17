num = int(input())

for _ in range(num):
  p1,p2 = input().split()
  p1 = sorted(p1)
  p2 = sorted(p2)
  if p1 == p2:
    print("Possible")
  else:
    print("Impossible")
