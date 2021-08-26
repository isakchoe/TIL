

def cnn(matrix):
    # 1*1 이면 리턴
    if len(matrix) == 1:
        return matrix[0][0]

    m = len(matrix)
    k = m//2

    # 리턴 행렬
    result = [[0]*(k) for _ in range(k)]

    for i in range(0,m,2):
        for j in range(0,m,2):
            # 2번째로 큰 수 구하기
            temp = sorted([matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]])
            temp = temp[-2]
            result[i//2][j//2] = temp
    # 재귀이용
    return cnn(result)



# 입력
n = int(input())

matrix = []

# 행렬 세팅
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# 출력
print(cnn(matrix))


