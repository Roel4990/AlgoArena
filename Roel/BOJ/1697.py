import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

visited = [False] * 100001

def bfs():
    queue = deque()
    queue.append((N, 0))
    visited[N] = True

    while queue:
        pos, time = queue.popleft()

        if pos == K:
            return time

        for next_pos in [pos - 1, pos + 1, pos * 2]:
            if 0 <= next_pos < 100001 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

    return None

print(bfs())