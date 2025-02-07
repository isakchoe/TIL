
from collections import deque

N = int(input())

matrix  = []

for _ in range(N):
    arr = list(map(int, input()))
    matrix.append(arr)


def bfs(row ,col):
    q = deque()
    q.append([row ,col])

    count = 0

    while q:
        r, c = q.popleft()
        count += 1

        dx = [0 ,0 ,1 ,-1]
        dy = [1 ,-1 ,0 ,0]

        for i in range(4):
            nx = dx[i] + r
            ny = dy[i] + c
            if 0<= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == 1:
                    count += 1
                    q.append([nx, ny])
    return count


answer = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for n in answer:
    print(n)

