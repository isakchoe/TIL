
# 입력받기
# 개수, 목표 금액
n, m = map(int, input().split())

money = []
for i in range(n):
    money.append(int(input()))

dp = [10001] *(10001)

dp[0] = 0

for i in range(n):
    # 화폐단위 시작부터, m 금액까지만 탐색
    for j in range( money[i], m+1):
        dp[j] = min(dp[j], dp[j -money[i]] + 1)



# 출력
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])