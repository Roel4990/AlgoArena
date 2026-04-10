import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0
for np in A:
    np -= B
    cnt += 1
    if np <= 0:
        continue
    cnt += (np + C - 1) // C

print(cnt)