import sys

input = sys.stdin.readline

T = int(input())
dp = [0] * 11

def f(n):
    if dp[n]:
        return dp[n]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return f(n - 1) + f(n - 2) + f(n - 3)


for _ in range(T):
    n = int(input())
    print(f(n))
