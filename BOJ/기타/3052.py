# 집합으로 푼 
arr = set()
for _ in range(0,10):
    N = int(input())
    arr.add(N%42)

print(len(arr))
