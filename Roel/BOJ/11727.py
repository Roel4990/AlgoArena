import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)

dp[1] = 1
if N >= 2: dp[2] = 3

def f(n):
    if dp[n]:
        return dp[n]
    dp[n] = (f(n - 1) + 2*f(n - 2)) % 10007
    return dp[n] % 10007

print(f(N))