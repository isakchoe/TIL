
t = int(input())

for tc in range(t):
    n, m = map(int, input().split())

    dp = []

    data = list(map(int, input().split()))


    index = 0


    # 초기 테이블 세팅
    for i in range(n):
        dp.append(data[index:index+m])
        index += m


    for col in range(1,m):

        for row in range(n):

            if row -1 >=0:
                up = dp[row-1][col-1]
            else:
                up = dp[row][col-1]

            if row +1 <n:
                down = dp[row+1][col-1]
            else:
                down = dp[row][col-1]
            # 점화식
            dp[row][col] += max(up,down, dp[row][col-1])


    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)



