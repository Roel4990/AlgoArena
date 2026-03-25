import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

# walk: x-1, x+1
# teleport: 2*x
q = deque()
q.append(n)
limit = 100000
# record the step to reach point
visited = [-1] * (limit + 1)

# start point
visited[n] = 0

while (q):
    curr = q.popleft()
    #print(f"curr: {curr}, visited: {visited[curr]}")
    if (curr == k):
        print(visited[k])
        break
    for nxt in (curr-1, curr+1, curr*2):
        # check valid range AND if it's not visited
        if 0 <= nxt <= limit and visited[nxt] == -1:
            q.append(nxt)
            # it can be reached with "visited[curr] + 1" step
            visited[nxt] = visited[curr] + 1
