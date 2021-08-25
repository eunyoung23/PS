import heapq,sys

input = sys.stdin.readline
s = set()

for _ in range(int(input())):
    name,el = input().split()
    if el == 'enter':
        s.add(name)
    else:
        s.remove(name)
