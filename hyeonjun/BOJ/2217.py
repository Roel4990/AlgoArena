import sys
input = sys.stdin.readline

n = int(input())
weights = [int(input()) for _ in range(n)]
weights.sort()
w = []

for i in range(n):
    w.append(weights[i] * (n - i))

print(max(w))