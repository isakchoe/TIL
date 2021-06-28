from collections import deque

n,m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

q = deque()

q.append([0,0])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

while q:
    r, c = q.popleft()

    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]

        if  0<= nr < n and 0<= nc < m:
            if graph[nr][nc] == 1:
                graph[nr][nc] = graph[r][c] + 1
                q.append([nr,nc])

print(graph[n-1][m-1])

