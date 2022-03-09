
# 회전함수 구현
# 회전함수 --> for 문 탐색하면서, 가장 작은값 리스트에 담기


def rotate(query, matrix):

    r1 = query[0 ] -1
    c1 = query[1 ] -1
    r2 = query[2 ] -1
    c2 = query[3 ] -1

    # 꼭지점 값 미리 세팅
    left_up = matrix[r1][c1]
    left_down = matrix[r2][c1]
    right_up = matrix[r1][c2]
    right_down = matrix[r2][c2]

    min_value = left_up

    for i in range(r1, r2 +1):
        for j in range(c1, c2 +1):
            if (i == r1 or i == r2 or j == c1 or j == c2):
                min_value = min(matrix[i][j], min_value)

    # 위
    for i in range(c2, c1, -1):
        matrix[r1][i] = matrix[r1][ i -1]
    # 아래
    for i in range(c1, c2):
        matrix[r2][i] = matrix[r2][ i +1]
    # 오른쪽
    for i in range(r2, r1 +1, -1):
        matrix[i][c2] = matrix[ i -1][c2]
    matrix[r1 +1][c2] = right_up
    # 왼쪽
    for i in range(r1, r2 -1):
        matrix[i][c1] = matrix[ i +1][c1]
    matrix[r2 -1][c1] = left_down

    return min_value


def solution(rows, columns, queries):

    matrix = [ [1 ] *columns for i in range(rows)]

    answer = []

    count = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = count
            count+= 1

    for query in queries:
        min_value = rotate(query, matrix)
        answer.append(min_value)

    return answer