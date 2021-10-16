

t = int(input())

for tc in range(1,t+1):
    # 입력
    n = int(input())

    # 행렬
    data = [[0] * 10 for _ in range(10)]

    count = 0

    for _ in range(n):
        r1,c1, r2, c2, color  = map(int, input().split())

        # red
        if color == 1:
            for i in range(r1,r2+1):
                for j in range(c1, c2 +1):
                    if data[i][j] == 2:
                        count += 1
                        data[i][j] = 3
                    else:
                        data[i][j] = 1
        # blue
        if color == 2:
            for i in range(r1,r2+1):
                for j in range(c1, c2 +1):
                    if data[i][j] == 1:
                        count += 1
                        data[i][j] = 3
                    else:
                        data[i][j] = 2


    print(f'#{tc} {count}')
