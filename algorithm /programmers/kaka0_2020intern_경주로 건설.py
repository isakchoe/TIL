import heapq


def solution(board):
    q = []

    n = len(board)

    cost_g = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                cost_g[i][j] = int(1e9)

    #     총 비용, 좌표, 경로
    heapq.heappush(q, [0, (0, 0), [(0,0)]])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]



    while q:
        dis, now, route = heapq.heappop(q)

        row = now[0]
        col = now[1]

        for i in range(4):
            nr = row + dx[i]
            nc = col + dy[i]
            #             범위안에 들고
            if 0 <= nr < n and 0 <= nc < n:
                #                 벽이 아니면
                if board[nr][nc] == 0:
                    route.append((nr, nc))
                    cost = dis + 100
                    if len(route) >= 3:
                        x = route[-3][0]
                        y = route[-3][1]
                        if abs(nr - x) == 1 and abs(nc - y) == 1:
                            cost += 500

                    # 재방문 여부는 총 비용으로 비교
                    if cost_g[nr][nc] > cost:
                        cost_g[nr][nc] = cost
                        heapq.heappush(q, (cost, (nr, nc), route))

    answer = cost_g[n - 1][n - 1]
    return answer