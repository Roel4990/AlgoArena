import sys
input = sys.stdin.readline

N = int(input())

deg = [0]*(N+1)
edges = []

for _ in range(N-1):
    u, v = map(int, input().split())
    edges.append((u, v))
    deg[u] += 1
    deg[v] += 1

def comb2(x):
    if x < 2:
        return 0
    return x*(x-1)//2

ans = 0

for u, v in edges:
    ans += comb2(deg[u]-1) * comb2(deg[v]-1)

print(ans)