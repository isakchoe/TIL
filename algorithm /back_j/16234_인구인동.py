
from collections import deque

# BFS 이용

def bfs(row,col):
    q = deque()
    q.append([row,col])

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    union_list = [[row,col]]
    visited[row][col] = True
    union_length = 0
    total = 0

    while q:
        r,c = q.popleft()

        union_length += 1
        now = data[r][c]
        total += now

        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]

            # 범위확인
            if 0<= nr < n and 0<=nc < n:

#                 조건 확인
                if left<= abs(data[nr][nc] - now) <=right and visited[nr][nc] == False:
                    union_list.append([nr,nc])
                    q.append([nr,nc])
                    visited[nr][nc] = True

    # 인구이동
    union_value = total//union_length
    for x,y in union_list:
        data[x][y] = union_value

    if union_length == 1:
        return False
    return True




# 입력
n,left,right = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

count = 0

while True:
    visited = [[False] * n for _ in range(n)]
    pivot = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                bfs(i,j)
                pivot += 1

    # 더 이상 인구이동이 일어나지 않으면, while 문 탈출
    if pivot == n*n:
        break
    # 인구이동이 있다면, 카운트 ++ 하고 다시 반복
    count+= 1


print(count)




