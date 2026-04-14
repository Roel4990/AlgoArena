import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

inc = [1] * N
dec = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            inc[i] = max(inc[i], inc[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if A[j] < A[i]:
            dec[i] = max(dec[i], dec[j] + 1)

answer = 0
for i in range(N):
    answer = max(answer, inc[i] + dec[i] - 1)

print(answer)