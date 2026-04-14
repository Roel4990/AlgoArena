import sys
from collections import deque
input = sys.stdin.readline
N, M, K = map(int, input().split())

graph = [[0] * (M + 1) for _ in range(N + 1)]

for _ in range(K):
    a, b = map(int, input().split())
    graph[a][b] = 1

visited = [[False] * (M + 1) for _ in range(N + 1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    size = 1
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 1 <= nx <= N and 1 <= ny <= M:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    size += 1
    return size

result = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] == 1 and not visited[i][j]:
            result = max(result, bfs(i, j))

print(result)
