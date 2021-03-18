from _collections import deque

t = int(input())

for _ in range(t):

    n = int(input())

    data = []
    data_check = [[0]*n for _ in range(n)]
    data_result = [[0]*n for _ in range(n)]


    for i in range(n):
        temp = list(map(int, input().split()))
        data.append(temp)

    for i in range(n):
        for e in range(n):
            data_result[i][e] = data[i][e]




    q = deque()
    q.append((0,0))

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        x, y = q.popleft()

        for e in range(4):

            n_x, n_y = x+dx[e], y+dy[e]

            if n_x >= 0 and n_x <n and n_y>=0 and n_y < n:
                if data_check[n_x][n_y] ==0:
                    data_result[n_x][n_y] = data_result[x][y] + data[n_x][n_y]
                    data_check[n_x][n_y] = 1
                    q.append((n_x,n_y))

                else:
                    data_result[n_x][n_y] = min(data_result[n_x][n_y], data_result[x][y]+data[n_x][n_y])

            else:
                continue

    print(data_result[n-1][n-1])


