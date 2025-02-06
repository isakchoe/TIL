


n = int(input())

matrix = []

for i in range(n):
    arr = list(map(int, (input().split())))
    matrix.append(arr)


# visited = [[False]*n for _ in range(n)]
# answer = 0
#
#
# def dfs(row, col, total,depth):
#     global answer
#
#     if depth > 4:
#         return total
#
#     total += matrix[row][col]
#     print(total, depth)
#
#     dx = [0,0,1,-1]
#     dy = [1,-1,0,0]
#
#     for k in range(4):
#         nx = row + dx[k]
#         ny = col + dy[k]
#
#         if 0<= nx < n and 0<= ny < n:
#             if not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 total += matrix[nx][ny]
#                 answer = max(answer, total)
#
#                 for i in range(n):
#                     for j in range(n):
#                         if not visited[i][j]:
#                             visited[i][j] = True
#                             dfs(i, j, total,depth+1)
#                             visited[i][j] = False
#
#                 total -= matrix[nx][ny]
#                 visited[nx][ny] = False
#
#
#
# for i in range(n):
#     for j in range(n):
#         visited[i][j] = True
#         dfs(i,j,0,0)
#         visited[i][j] = False

from itertools import combinations

answer = 0

if n == 2:
    answer += sum(matrix[0])
    answer += sum(matrix[1])

else:
    # 모든 쌍.
    tree_combi = []
    dx = [1,0]
    dy = [0,1]

    for i in range(n):
        for j in range(n):
            for k in range(2):
                nx = dx[k] + i
                ny = dy[k] + j

                if 0 <= nx < n and 0 <= ny < n:
                    tree_combi.append([[i,j], [nx,ny], matrix[i][j] + matrix[nx][ny]])


    # 조경 횟수 1~4
    for r in range(1,5):
        #  각 경우의 수에서 합 구하기
        for combi in list(combinations(tree_combi, r)):
            used = set()
            valid = True

            total = 0

            for [r,c], [r2,c2], value in combi:

                if (r,c) in used or (r2,c2) in used:
                    valid = False
                    break

                # 방문처리
                used.add((r,c))
                used.add((r2,c2))
                total += value

            if valid:
                answer = max(answer, total)
print(answer)













