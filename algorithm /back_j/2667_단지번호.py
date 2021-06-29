from collections import deque

# bfs 함수 만들기
# for 문 돌면서 각 행열에 대해 bfs 실행,, 조건 성립할때 단지수 ++
#  return 값으로 단지내 아파트 수

# 압력처리
n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int,input())))


# 방문처리
visited = [[False]*n for _ in range(n)]

def bfs(r,c):
    # 본인포함
    count = 1
    q = deque()
    q.append([r,c])

    visited[r][c] = True

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y +dy[i]
            # 범위안
            if 0<=nx < n and 0<=ny<n :
                # 집이 존재하고, 첫방문일때
                if graph[nx][ny] ==1 and visited[nx][ny] == False:
                    count += 1
                    visited[nx][ny] = True
                    q.append([nx,ny])

    return count



# 탐색

total = 0
count_list = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            total += 1
            count = bfs(i,j)
            count_list.append(count)

print(total)
count_list.sort()
for c in count_list:
    print(c)



