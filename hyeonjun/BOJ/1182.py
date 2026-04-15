import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

def dfs(index, current_sum):
    global count
    if index == N:
        if current_sum == S:
            count += 1
        return
    
    dfs(index + 1, current_sum + arr[index])
    dfs(index + 1, current_sum)

dfs(0, 0)

if S == 0:
    count -= 1

print(count)