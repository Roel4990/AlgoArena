import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y):
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    while queue:
        cx, cy, cnt = queue.popleft()
        if cx == endX and cy == endY:
            return cnt
        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < I and 0 <= ny < I:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cnt + 1))
    return None

for _ in range(T):
    I = int(input())
    visited = [[False] * (I+1) for _ in range(I+1)]
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())
    print(bfs(startX, startY))
