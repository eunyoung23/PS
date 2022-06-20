import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    result = True

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def dfs(x, color):
        global result
        if color == True:
            visited[x] = 1
        if color == False:
            visited[x] = 2

        for i in graph[x]:
            if visited[i]!=0:
                if visited[x] == visited[i]:
                    result = False
                    return
            else:
                if visited[i]==0:
                    dfs(i, not color)
                else:
                    return

    dfs(1, False)

    if result == True:
        print("YES")
    else:
        print("NO")
