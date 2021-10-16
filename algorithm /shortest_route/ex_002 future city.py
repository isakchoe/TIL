
INF = int(1e9)

n, m = map(int, input().split())


data = [[INF]*(n+1) for _ in range(n+1)]



for i in range(1,n+1):
    for e in range(1,n+1):
        if i == e:
            data[i][e] = 0



for i in range(m):
    a, b = map(int, input().split())
    data[a][b] = 1
    data[b][a] = 1


x, k = map(int,input().split())

for q in range(1,n+1):
    for w in range(1,n+1):
        for e in range(1,n+1):
            data[w][e] = min(data[w][e], data[w][q] + data[q][e])

# k방문하고 x로 가는 최단거리

result = data[1][k] + data[k][x]


for i in range(1,n+1):
    for e in range(1,n+1):
        print(data[i][e])

    print("-- ")


if result >= INF:
    print(-1)
else:
    print(result)
