
from collections import deque
from itertools import  combinations



n,m = map(int, input().split())

data = []


# 데이터 복사할 temp
temp_data = [[0]*m for _ in range(n)]




for i in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)


def bfs(data):

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    q = deque()


    for i in range(n):
        for e in range(m):
            if data[i][e] == 2:
                q.append((i,e))


    while q:

        row, col = q.popleft()


        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]

            if nx <0 or nx >=n or ny <0 or ny>=m:
                continue

            if  data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx,ny))


    # 안전구역 출력까지 한번에

    total = 0

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                total += 1


    return total



blank = []



for i in range(n):
    for e in range(m):
        if data[i][e] == 0 :
            blank.append([i,e])


# 벽을 세울 수 있는 모든 경우의 수 == 조합
result = list(combinations(blank,3))




answer = -1

for combis in result:

    for a in range(n):
        for b in range(m):
            temp_data[a][b] = data[a][b]


    for i in combis:
        temp_data[i[0]][i[1]] = 1

    temp_result = bfs(temp_data)
    answer = max(answer, temp_result)




print(answer)




