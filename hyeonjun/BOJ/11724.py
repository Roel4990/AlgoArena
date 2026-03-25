# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)  # 재귀 제한을 100만으로 늘림

# n, m = map(int, input().split())

# graph = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)
# cnt = 0

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# #print(graph)

# def dfs(n):
#     if visited[n] == False:
#         visited[n] = True
#         for i in graph[n]:
#             dfs(i)

# for i in range(1, n + 1):
#     if not visited[i]:
#         cnt += 1
#         dfs(i)

# print(cnt)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    stack = [start]
    while stack:
        n = stack.pop()
        if not visited[n]:
            visited[n] = True
            for i in graph[n]:
                stack.append(i)

for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)