import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))

    adj_list = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    for _ in range(K):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        indegree[v] += 1

    W = int(input())

    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = D[i - 1]

    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        cur = queue.popleft()
        for nxt in adj_list[cur]:
            dp[nxt] = max(dp[nxt], dp[cur] + D[nxt - 1])
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    print(dp[W])