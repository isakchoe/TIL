

# 입력 받기

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    # 골드 그래프이자, dp 테이블
    gold = []
    temp = list(map(int, input().split()))

    for i in range(0, n*m, m):
        gold.append(temp[i: i+m])


    # 작업

    for col in range(1, m):
        for row in range(n):
            now = gold[row][col]

            # 위
            if 0<=row-1<n:
                up = gold[row-1][col-1]
            else:
                up = 0


            # 옆
            side = gold[row][col-1]

            # 아래
            if 0<= row+1 <n:
                down = gold[row+1][col-1]
            else:
                down = 0

            # 점화식
            gold[row][col] = max(up+now, side +now, down +now)


    #         출력
    answer = 0

    for i in range(n):
        if gold[i][m-1] > answer:
            answer = gold[i][m-1]

    print(answer)





