

n,m,round = map(int, input().split())

matrix = []

for _ in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

attacks = []
defends = []

for _ in range(round):
    r, c, direction = input().split()
    attacks.append([int(r),int(c),direction])

    row, col = map(int, input().split())
    defends.append([row, col])


score = 0

for j in range(round):
    r,c,direction = attacks[j]
    r -= 1
    c -= 1

    length = matrix[r][c]

    # 북
    if direction == "N":
        end = r+1 - length
        if end >0:
            while r >= end:
                if r +1 - matrix[r][c] < end :
                    if r +1 - matrix[r][c] <= 0:
                        end = 0
                    else:
                        end = r+1- matrix[r][c]
                if matrix[r][c] > 0:
                    matrix[r][c] = - matrix[r][c]
                    score += 1
                r -= 1

        # 전부다 쓰러지는 경우
        else:
            score += length
            for i in range(r, -1, -1):
                matrix[i][c] = -matrix[i][c]

    # 남
    if direction == "S":
        end = r-1 + length
        if end < n:
            while r <= end:
                if r-1 + matrix[r][c] > end:
                    if r -1 +  matrix[r][c] >= n-1:
                        end = n-1
                    else:
                        end = r-1+ matrix[r][c]

                if matrix[r][c] > 0:
                    matrix[r][c] = - matrix[r][c]
                    score += 1
                r += 1

        # 전부다 쓰러지는 경우
        else:
            score += length
            for i in range(r, n):
                matrix[i][c] = -matrix[i][c]

    # 서
    if direction == "W":
        end = c +1 -  length

        if end  > 0:
            while c >= end:
                if c +1 - matrix[r][c] < end:
                    if c + 1 - matrix[r][c] <= 0:
                        end = 0
                    else:
                        end = c + 1 - matrix[r][c]
                if matrix[r][c] > 0:
                    matrix[r][c] = - matrix[r][c]
                    score += 1
                c -= 1

        else:
            score += length
            for i in range(c, -1, -1):
                matrix[r][i] = - matrix[r][i]

    if direction == "E":
        end = c + length - 1

        if end < m-1:
            while c <= end:
                if c -1 + length > end:
                    if c -1 + length >= m-1:
                        end = m-1
                    else:
                        end = c-1 + length

                if matrix[r][c] > 0:
                    matrix[r][c] = - matrix[r][c]
                    score += 1
                c += 1


        else:
            score +=length
            for i in range(c, m):
                matrix[r][i] = - matrix[r][i]


    # 수비
    dr, dc = defends[j]
    matrix[dr-1][dc-1] = abs(matrix[dr-1][dc-1])


print(score)

for i in range(n):
    for j in range(m):
        if matrix[i][j] < 0:
            print("F", end=" ")
        else:
            print("S", end=" ")
    print()


