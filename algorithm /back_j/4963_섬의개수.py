
from collections import deque

#  그래프 만들기
# bfs 함수 만들기 ==> 대각선까지 포함
#  모든 행열 탐색하면서 bfs 시도 ==> 섬 개수 count


def bfs(r,c):
    q = deque()
    q.append([r,c])

    while q:
        x,y = q.popleft()

        dx = [0,0,1,-1,-1,-1,1,1]
        dy = [1,-1,0,0,1,-1,-1,1]

        for i in range(8):
            nr = x + dx[i]
            nc = y + dy[i]

#             범위
            if 0<=nr< h and 0<=nc<w:
                if graph[nr][nc] == 1:
                    # 방문처리
                    graph[nr][nc] = 0
                    q.append([nr,nc])


answer = []

# 입력
while True:
    w, h  = map(int,input().split())

    if w==0 and h == 0 :
        for i in answer:
            print(i)
        break

    graph = []

    for _ in range(h):
        graph.append(list(map(int,input().split())))


    count = 0

    for i in range(h):
        for j in range(w):
            # 땅이라면
            if graph[i][j] == 1:
                count += 1
                bfs(i,j)

    # 삽입
    answer.append(count)





