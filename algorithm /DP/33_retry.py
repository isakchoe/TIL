
# 입력

n = int(input())
time = [0]
money = [0]

for _ in range(n):
    a, b = map(int, input().split())
    time.append(a)
    money.append(b)


dp = [-1] * (n+2)
dp[n+1] = 0

max_value = 0

for i in range(n,0,-1):
    # i +1 날에 상담 시작해도 퇴사전까지 완료 못하는 경우
    if i + time[i] > n+1:
        dp[i] = dp[i+1]

    # i+1 날에 시작해서 퇴사전까지 완료할 수 있는 경우 ==> 그날 상담하고 완료한뒤 값 vs dp[i+2] 비교
    else:
        dp[i] = max(money[i] + dp[i+time[i]], dp[i+1])


print(dp[1])

