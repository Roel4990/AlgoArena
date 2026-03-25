import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
def f(n):
    if dp[n]:
        return dp[n]
    dp[n] = f(n - 1) + f(n - 2) + f(n - 3)
    return dp[n]
for _ in range(T):
    n = int(input())
    print(f(n))
