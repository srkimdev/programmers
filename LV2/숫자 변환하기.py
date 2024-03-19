def solution(x, y, n):
    answer = 0
    
    INF = int(1e9)
    
    dp = [INF] * (y + 1)
    dp[x] = 0

    for i in range(x, y + 1):
        
        if i % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i])
    
        if i % 3 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i])

        if i >= n:
            dp[i] = min(dp[i - n] + 1, dp[i])

    if dp[y] == INF:
        return -1
    else:
        return dp[y]