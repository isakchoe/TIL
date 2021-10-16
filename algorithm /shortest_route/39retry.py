
import heapq

t = int(input())

for tc in range(t):

    n = int(input())

    # 간선 그래프
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))


    # distance 그래프
    INF = int(1e9)
    dis = [[INF] * (n) for _ in range(n)]

    # 힙큐, 시작 삽입    (거리, 좌표)
    q = []
    heapq.heappush(q, (graph[0][0], (0,0)))
    dis[0][0] = graph[0][0]


    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        distance, now = heapq.heappop(q)
        row = now[0]
        col = now[1]

        # 스킵하는 경우
        if dis[row][col] < distance:
            continue

        for i in range(4):
            nr = row + dx[i]
            nc = col + dy[i]

            if 0 <= nr <n and 0<= nc <n:
                cost = distance + graph[nr][nc]
                # cost 갱신
                if dis[nr][nc] > cost:
                    dis[nr][nc] = cost
                    heapq.heappush(q, (cost, (nr,nc)))


    # 출력
    print(dis[n-1][n-1])
