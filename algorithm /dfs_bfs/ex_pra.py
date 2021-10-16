from _collections import deque

n, m = map(int, input().split())

print(n)

graph = []

for i in range(n):
    temp = list(map(int, input()))
    graph.append(temp)




def bfs(d_row, d_col):
    q = deque()
    q.append((0, 0))

    result = 0

    move_row = [-1, 1, 0, 0]
    move_col = [0, 0, -1, 1]

    while q:
        p_r, p_c = q.popleft()

        for i in range(4):
            n_r = p_r + move_row[i]
            n_c = p_c + move_col[i]

            # 범위 벗어나는 경우
            if n_r < 0 or n_r >= n or n_c < 0 or n_c >= m:
                continue

            if graph[n_r][n_c] == 0:
                continue

            if graph[n_r][n_c] == 1:
                graph[n_r][n_c] = graph[p_r][p_c] + 1
                q.append((n_r,n_c))



    print(graph[d_row-1][d_col-1])



bfs(n,m)