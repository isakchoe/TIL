

str1 = input()
str2 = input()

def distance(now, target):

    n = len(now)
    m = len(target)

    # dp[0][0] = 0  중요! ===> dp[i][j] ==>  now[:i] 까지를 target[:j] 까지 바꾸는데 걸리는 횟수
    dp = [[0]*(m+1) for _ in range(n+1)]

    # 세팅

    for i in range(1,n+1):
        dp[i][0] = i

    for j in range(1, m+1):
        dp[0][j] = j

    # 점화식

    for i in range(1, n+1):
        for j in range(1, m+1):
            # 문자가 같은 경우
            if now[i-1] == target[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # 아닌 경우, 왼쪽, 왼쪽위, 위 에서 +1,,, 가장 작은거 선택
            else:
                dp[i][j] = min(dp[i-1][j-1] +1 , dp[i-1][j]+1,dp[i][j-1]+1)

    return dp[n][m]


print(distance(str1,str2))