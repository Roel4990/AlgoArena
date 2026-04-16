import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
else:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        # 세로타일 1개 추가: i - 1
        # 가로타일 2개 추가: i - 2
        dp[i] = (dp[i-1] + dp[i-2])%10007

    print(dp[n])