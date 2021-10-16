from _collections import deque


# 입력받기
n,l,r = map(int, input().split())


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 행열 입력 받기
data =[]
for i in range(n):
    data.append(list(map(int, input().split())))



def bfs(row, col):

    q = deque()

    # 큐에 삽입, 방문 처리
    q.append((row, col))
    visited[row][col] = 1

    # 연합 리스트 위치 정보, 연합 인구 합!!
    union_list =[(row,col)]
    total = 0

    while q:
        x, y = q.popleft()

        total += data[x][y]

        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]

            # 좌표 안에 들어가고, 방문한적 없으면
            if nx >=0 and nx <n and ny >= 0 and ny <n and visited[nx][ny] == -1:
                # 조건 만족하면 큐에삽입, 방문처리
                if l <= abs(data[nx][ny] - data[x][y]) <= r:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    union_list.append((nx,ny))

    # 연합 나라들 인구 이동 (볌수 처리)
    for i,j in union_list:
        data[i][j] = total//len(union_list)





total_count = 0


# 모든 위치에 대해서 bfs를 실행 -> but bfs 실행으로 그룹이 형성되면 형성된 인덱스는 스킵한다. ->

while True:
    # 방문여부 변수
    visited = [[-1]*n  for _ in range(n)]
    index = 0
    for i in range(n):
        for e in range(n):
            if visited[i][e] == -1:
                bfs(i,e)
                index += 1



    # 더 이상 이동 없는 경우(핵심!)
    if index == n*n:
        break

    total_count += 1


print(total_count)






