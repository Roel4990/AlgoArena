import sys

# 예제.txt
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

N = int(input())

# dp 리스트 생성
dp = [(0,0)] * 41
dp[0] = (1,0)
dp[1] = (0,1)

# 40보다 작거나 같은 자연수 또는 0
for i in range(2,41):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])
# dp[0] ~ dp[40]까지 값이 이미 dp 리스트에 저장되어있음
# 아래 for 문으로 해당 값만 꺼내면 끝

# _는 변수 안 쓸 때
for _ in range(N):
    n = int(input())
    print(dp[n][0], dp[n][1])