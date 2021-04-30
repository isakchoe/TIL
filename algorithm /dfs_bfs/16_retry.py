from _collections import deque
from  itertools import combinations


# 입력
n,m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))


# 벽을 세우는 모든 경우의 수 조사하기. 조합으로!
pre_list = []
virus_list =[ ]

# 빈공간, 바이러스 위치 따로 삽입
for i in range(n):
    for e in range(m):
        if graph[i][e] == 0:
            pre_list.append((i,e))
        if graph[i][e] == 2:
            virus_list.append((i,e))


combi = list(combinations(pre_list,3))


def bfs(data):
    q = deque()
    # 초기 세팅, 바이러스들 큐에 삽입
    for i in range(len(virus_list)):
        q.append(virus_list[i])


    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        row, col = q.popleft()

        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]

            if nx >=0 and nx < n and ny>=0 and ny <m:
                # 감염
                if data[nx][ny] == 0 :
                    data[nx][ny] = 2
                    q.append((nx,ny))

    # 감염안된 영역 카운트
    answer = 0

    for i in range(n):
        for e in range(m):
            if data[i][e] == 0:
                answer += 1

    return answer

# 조합 수행

answer = 0

for i in range(len(combi)):
    temp = combi[i]


    # 임시 그래프 만들기
    data = [[0]*m for _ in range(n)]
    for j in range(n):
        for s in range(m):
            data[j][s] = graph[j][s]

    # 기둥 설치
    for x,y in temp:
        data[x][y] = 1

    # bfs 수행
    result = bfs(data)

    if answer < result:
        answer = result

# 출력
print(answer)