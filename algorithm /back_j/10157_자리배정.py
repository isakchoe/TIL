

c, r = map(int, input().split())
k = int(input())


# 행렬만들기, 넘버링 불일치!
matrix = [[0]*c for _ in range(r)]

# 상,우,하,좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# 처음세팅
matrix[r-1][0] = 1
pre_row, pre_col = r-1, 0

index = 0
number = 2

while True:
    new_r = pre_row + dr[index%4]
    new_c = pre_col + dc[index%4]

    # 범위확인, 방문여부 확인
    if 0<=new_r < r and 0<=new_c<c and matrix[new_r][new_c] ==0:
        # 넘버링
        matrix[new_r][new_c] = number
        # 다음숫자 증가
        number += 1

        # 더이상 앉을 자리 없다
        if number > r*c:
            break

        # 갱신작업
        pre_row = new_r
        pre_col = new_c

    # 범위벗어나면 다른 익데스로
    else:
        index += 1



if k > r*c:
    print(0)
else:
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == k:
                # row == y (방향도 다르다, 아래에서 위로 커지는 경우) , col == x (방향 같다)
                print(j+1, r- i )
                break

