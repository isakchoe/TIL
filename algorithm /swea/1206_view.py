


for tc in range(1,11):
    n = int(input())
    arr = list(map(int, input().split()))
    col = max(arr)

    # 행렬 생성
    matrix = [ ]

    for num in arr:
        temp = [0] * col
        for i in range(num):
            temp[i] = 1

        matrix.append(temp)

    count = 0
#     행렬탐색하면서,
    for i in range(2, n-2):
        for j in range(col):
            # 세대가 있으면, 위 아래 두칸 여부 확인
            if matrix[i][j] == 1:
                if matrix[i-1][j] ==0 and matrix[i-2][j] == 0 and matrix[i+1][j] == 0 and matrix[i+2][j] == 0:
                    count += 1

    print(count)