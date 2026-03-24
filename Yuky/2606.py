import sys
input = sys.stdin.readline

# 컴퓨터 수
n = int(input())
# 쌍의 수
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = True
    next_node = graph[node]
    count = 1

    for n in next_node:
        if visited[n] == False:
            count += dfs(n)
    
    return count

print(dfs(1)-1)
        

