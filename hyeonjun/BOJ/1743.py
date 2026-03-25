import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
way = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
visited = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
answer = []
cnt = 0

for _ in range(k):
    x, y = map(int, input().split())
    way[x][y] = 1

def dfs(x, y):
    global cnt
    stack = [(x, y)]
    visited[x][y] = 1
    while stack:
        cx, cy = stack.pop()
        cnt += 1
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = cx+dx, cy+dy
            if way[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                stack.append((nx, ny))

for i in range(1, n+1):
    for j in range(1, m+1):
        if way[i][j] == 1:
            dfs(i, j)
            answer.append(cnt)
            cnt = 0

print(max(answer))