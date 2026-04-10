import sys

input = sys.stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]

ropes.sort()

sum = 0
for i in range(N):
    if sum < ropes[i] * (N - i):
        sum = ropes[i] * (N - i)

print(sum)