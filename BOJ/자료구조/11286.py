import heapq, sys

input = sys.stdin.readline
hq = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(hq, (abs(x), x))
    else:
        print(heapq.heappop(hq)[1] if hq else 0)
