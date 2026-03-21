import sys
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N + 1)]
cnt = 0

for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for i in edges:
    if len(i) >= 3:
        a = len(i) - 1

        for j in i:
            if len(edges[j]) >= 3:
                b = len(edges[j]) - 1

                cnt += (a * b * (a - 1) * (b - 1) / 4)

print(int(cnt/2))