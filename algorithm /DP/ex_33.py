


n = int(input())

time = []
profit = []

dp = [0]*(n+1)

for i in range(n):
    x,y = map(int, input().split())
    time.append(x)
    profit.append(y)

max_value = 0

for i in range(n-1,-1,-1):

    next = i + time[i]

    if next <=n:

        dp[i] = max(max_value, profit[i] + dp[next])
        max_value = dp[i]

    else:
        dp[i] = max_value


print(max_value)
