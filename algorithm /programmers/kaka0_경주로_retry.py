from collections import deque
import copy

def solution(board):
    q = deque()

    n = len(board)

    cost_g = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                cost_g[i][j] = int(1e9)

    #     총 비용, 좌표, 경로
    q.append((0, (0, 0), [(0, 0)]))
    cost_g[0][0] = 0

    dx = [0, -1, 1, 0]
    dy = [1, 0, 0, -1]

    while q:
        dis, now, route = q.popleft()
        row = now[0]
        col = now[1]

        if cost_g[row][col] < dis:
            continue

        for i in range(4):
            nr = row + dx[i]
            nc = col + dy[i]
            #             범위안에 들고
            if 0 <= nr < n and 0 <= nc < n:
                #                 벽이 아니면
                if board[nr][nc] == 0:
                    # route 가 변하네,,,, 변하지 않게!!

                    print((nr,nc))
                    new_route = copy.deepcopy(route)
                    new_route.append((nr,nc))


                    cost = dis + 100
                    if len(new_route) >= 3:
                        x = new_route[-3][0]
                        y = new_route[-3][1]

                        if abs(nr - x) == 1 and abs(nc - y) == 1:
                            # print(nr,nc)
                            cost += 500
                            # print(cost)

                    # 재방문 여부는 총 비용으로 비교
                    if cost_g[nr][nc] >= cost:

                        cost_g[nr][nc] = cost
                        q.append((cost, (nr, nc), new_route))


    for i in range(n):
        print(cost_g[i])

    answer = cost_g[n - 1][n - 1]
    return answer



board = [
	[0, 0, 1, 0, 1, 1, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 1, 1, 0, 1],[1, 0, 0, 0, 0, 1, 1, 0, 1, 0],[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 1, 0, 1, 0, 1, 1],[0, 0, 1, 0, 1, 1, 0, 1, 0, 1],[0, 1, 0, 0, 1, 0, 0, 0, 1, 0],[1, 0, 0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 1, 0, 1, 0, 0],[1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

print(solution(board))