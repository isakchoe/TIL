
# 입력받기
n = int(input())
food = list(map(int, input().split()))

# 테이블 세팅
dp = [0] *(n+1)

dp[1] = food[0]

# 점화식
for i in range(2, n+1):
    dp[i] = max(dp[i-2] + food[i-1], dp[i-1])


print(dp[n])
