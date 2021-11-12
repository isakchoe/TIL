

from collections import deque
from copy import deepcopy

# bfs

def bfs(row, col, matrix ):
    q = deque()
    # 초기세팅
    q.append([row,col, 0])
    temp_matrix = deepcopy(matrix)
    temp_matrix[row][col] = 'W'

    result_count = 0

    while q:
        r, c, count = q.popleft()

        if count > result_count:
            result_count = count

        dx = [0,0,1,-1]
        dy = [1,-1,0,0]

        for i in range(4):
            nr = r +dx[i]
            nc = c + dy[i]

            if 0<=nr < n and 0<=nc < m:
                if temp_matrix[nr][nc] == 'L':
                    temp_matrix[nr][nc] = 'W'
                    q.append([nr,nc, count + 1])

    return result_count



n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'L':
            count = bfs(i,j,matrix)
            if count > answer:
                answer = count

print(answer)
