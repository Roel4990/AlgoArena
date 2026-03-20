import sys
input = sys.stdin.readline

N = int(input())
m = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
cnt = 0

def dfs(x):
    global cnt

    cnt += 1
    visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            dfs(i)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(cnt - 1)