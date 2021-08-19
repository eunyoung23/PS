set1 = set()
set2 = set()

N,M = map(int,input().split())

for _ in range(N):
    set1.add(input())

for _ in range(M):
    set2.add(input())

result = sorted(set1 & set2)
print(len(result))

for i in range(len(result)):
    print(result[i])
