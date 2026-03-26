import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    l = int(input())
    cur_x, cur_y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    q = deque([(cur_x, cur_y)])
    visited = [[-1] * l for _ in range(l)]
    visited[cur_x][cur_y] = 0

    if cur_x == target_x and cur_y == target_y:
        print(0)
        continue

    found = False

    while q:
        cur_x, cur_y = q.popleft()

        for next_x, next_y in [(cur_x-2, cur_y-1), (cur_x-2, cur_y+1), (cur_x-1, cur_y-2), (cur_x-1, cur_y+2), 
                               (cur_x+1, cur_y-2), (cur_x+1, cur_y+2), (cur_x+2, cur_y-1), (cur_x+2, cur_y+1)]:
            if 0 <= next_x < l and 0 <= next_y < l and visited[next_x][next_y] == -1:
                visited[next_x][next_y] = visited[cur_x][cur_y] + 1
                q.append((next_x, next_y))

                if next_x == target_x and next_y == target_y:
                    print(visited[next_x][next_y])
                    found = True
                    break
        
        if found:
            break