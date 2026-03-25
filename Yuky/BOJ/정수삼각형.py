def solution(triangle):
    answer = 0
    # 꼭->아래 숫자의 합이 가장 큰 경우 
    # 아래 or 아래 + 1(대각선)
    dp = [ [0] * len(row) for row in triangle ]
    
    dp[0][0] = triangle[0][0]
    
    # 각 위치의 오기 까지의 최대 합
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            
            # left:
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
                #print(f"left: {dp[i][j]}")
            # right:
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                #print(f"right: {dp[i][j]}")
            # middle: up or up left
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
                #print(f"middle: {dp[i][j]}")
                
    return max(dp[-1])