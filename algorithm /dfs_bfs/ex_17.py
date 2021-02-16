
from _collections import deque

n,k = map(int, input().split())

data = []

for e in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)

s, x ,y = map(int, input().split())


def bfs():

    blank = []

    for i in range(n):
        for e in range(n):
            if data[i][e] != 0:
                blank.append([data[i][e], (i,e)])

    blank.sort( key = lambda x : x[0])

    q = deque()

    for i in range(len(blank)):
        q.append(blank[i][1])

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]


    while q:
        row, col = q.popleft()

        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]

            if nx <0 or nx >=n or ny<0 or ny>=n:
                continue

            if data[nx][ny] == 0 :
                data[nx][ny] = data[row][col]




for i in range(s):
    bfs()

print(data[x-1][y-1])

