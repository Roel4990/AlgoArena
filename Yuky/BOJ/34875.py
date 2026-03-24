
# 두 main node에 각각 연결된 child node가 두개씩
# 각 edge 마다 각각 연결된 node 수가 >= 2일때 2개를 뽑는 조합 

import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
count = 0

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for u in range(1, N+1):
    for v in graph[u]:
        # edge u-v
        n = len(graph[u])-1
        m = len(graph[v])-1
        if v < u :
            continue
        if  n > 1 and m > 1:
            w = (n*(n-1)) // 2
            z = (m*(m-1)) // 2
            count += (w*z)
            #print(f"u: {u}, v:{v}, nodes: {(n*(n-1)) // 2}, {(m*(m-1)) // 2}")

print(count)

    