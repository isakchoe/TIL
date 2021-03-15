


p = list(map(int, input().split()))
drop = list(map(int,input().split()))
tip = list(map(int,input().split()))


profit = []



for i in range(len(p)):
    temp = drop[i] - p[i] + tip[i]
    profit.append(temp)



# max_value 값 세팅, dp 테이블 세팅
dp = [0]*(len(p))

dp[len(p)-1] = profit[-1]
max_value = dp[len(p)-1]

for i in range(len(p)-2, -1,-1):
    for e in range(i+1,len(p)):
        if drop[i] > p[e]:
            if e == len(p)-1:
                dp[i] = max(max_value, profit[i])
                max_value = dp[i]
            else:
                continue
        else:
            dp[i] = max(max_value, dp[e] + profit[i])
            max_value = dp[i]

print(max_value)
