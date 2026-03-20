import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (N+1)
cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        stack = [i]
        visited[i] = True

        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

print(cnt)