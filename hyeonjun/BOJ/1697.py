import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = []
visited = [0] * 100001

queue.append(n)
visited[n] = 1

if n == k:
    print(0)
    
else:
    while queue:
        node = queue.pop(0)

        for next_node in [node-1, node+1, node*2]:
            if 0 <= next_node <= 100000:
                if visited[next_node] == 0:
                    visited[next_node] = visited[node] + 1
                    queue.append(next_node)

                    if next_node == k:
                        print(visited[next_node] - 1)