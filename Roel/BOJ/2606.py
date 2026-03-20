import sys
input = sys.stdin.readline

C = int(input())
N = int(input())

graph = [[] for _ in range(C + 1)]

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (C + 1)
visited[1] = True
stack = [1]
count = 0

while stack:
    node = stack.pop()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            count += 1
            stack.append(neighbor)

print(count)