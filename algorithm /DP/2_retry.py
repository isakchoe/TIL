
n = int(input())

INF = int(1e9)

# 초기 dp 테이블
dp = [INF] *(n+1)
dp[1] = 0

# 보틈업!
for i in range(2,n+1):

    if i%2 == 0 :
        dp[i] = min(dp[i//2] + 1, dp[i])

    if i%3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])

    if i%5 == 0:
        dp[i] = min(dp[i//5] +1, dp[i])

    dp[i] = min(dp[i-1] + 1, dp[i])

print(dp[n])

