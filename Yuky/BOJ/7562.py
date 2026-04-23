import sys
from collections import deque
#sys.stdin = open("input.txt","r")

input = sys.stdin.readline

dx = [-2,-2,2,2,-1,1,-1,1]
dy = [-1,1,-1,1,-2,-2,2,2]

# diagonal: dx+dy
# knight = straigth + diag

T = int(input())
q = deque()


for i in range(T):
    l = int(input())
    visited = [[ -1 for _ in range(l)] for _ in range(l)]
    x, y = map(int, input().split())
    #print(f"T: {i}, x,y: {x}, {y}")
    target_x, target_y = map(int, input().split())
    #print(f"target x, y: {target_x}, {target_y}")
    q.append((x,y))
    visited[x][y] = 0
    while(q):
        a, b = q.popleft()
        #print(f"a,b pop: {a}, {b}")
        if a == target_x and b == target_y:
            print(visited[a][b])
            q.clear()
            break
        for j in range(8):
            nx = a + dx[j]
            ny = b + dy[j]
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == -1:
                #print(f"append nx, ny: {nx}, {ny}")
                q.append((nx, ny))
                visited[nx][ny] = visited[a][b] + 1


