
INF = int(1e9)

n = int(input())
m = int(input())

data = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for e in range(1,n+1):
        if i == e:
            data[i][e] = 0


for i in range(m):
    a,b,c, = map(int,input().split())

    if data[a][b] > c:
        data[a][b] = c


for x in range(1,n+1):
    for y in range(1,n+1):
        for z in range(1,n+1):
            data[y][z] = min(data[y][z], data[y][x] + data[x][z])


for i in range(1,n+1):
    for e in range(1,n+1):
        print(data[i][e], end =' ')

    print(" ")

