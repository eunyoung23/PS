from itertools import combinations

tc = 0
while True:
    k,*s = map(int,input().split())

    if k==0:
        break

    if tc:
        print()

    for combi in combinations(s,6):
        print(*combi)

    tc+=1
