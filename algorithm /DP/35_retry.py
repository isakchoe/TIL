
n = int(input())

dp = [-1] *(n+1)

next_2 = 2
next_3 = 3
next_5 = 5
two_index = th_index = five_index = 1

dp[0] = 0
dp[1] = 1

for i in range(2, n+1):

    dp[i] = min(next_2, next_3, next_5)

    if dp[i] == next_2:
        two_index += 1
        next_2 = dp[two_index] * 2

    if dp[i] == next_3:
        th_index += 1
        next_3 = dp[th_index]*3

    if dp[i] == next_5:
        five_index += 1
        next_5 = dp[five_index]*5


print(dp)