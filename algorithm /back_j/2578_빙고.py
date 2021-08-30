

# 빙고 확인하는 함수 3개!

def check_matirx(matrix):

    answer = 0

    # 가로, 세로 확인
    for i in range(5):
        count = 0
        col_count = 0
        for j in range(5):
            # 가로줄
            if matrix[i][j] == 0 :
                count += 1
            # 세로줄
            if matrix[j][i] == 0:
                col_count += 1

        if count == 5:
            answer += 1

        if col_count == 5:
            answer += 1


    # 대각선
    slot_count = 0
    xy_count = 0
    for i in range(5):
        if matrix[i][i] == 0:
            slot_count += 1

        if matrix[i][4-i] == 0:
            xy_count += 1

    if slot_count == 5:
        answer += 1

    if xy_count == 5:
        answer += 1

    return answer






# 빙고 받기
matrix = []

for _ in range(5):
    matrix.append(list(map(int, input().split())))

numbers = []

for _ in range(5):
    a, b, c, d, e  = map(int, input().split())

    numbers.append(a)
    numbers.append(b)
    numbers.append(c)
    numbers.append(d)
    numbers.append(e)

answer = 0

# 사회자 번호 순서 == 넘버링 일치 안함
for idx, num in enumerate(numbers):
    pivot =  0
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == num:
                matrix[i][j] = 0
                pivot += 1
                break

        if pivot != 0:
            break

    # 빙고 개수 확인
    if check_matirx(matrix) >= 3:
        answer = idx +1
        break

print(answer)





