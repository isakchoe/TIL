
# 노드, 간선 입력받기
n = int(input())
m = int(input())


# 최단거리 2차원 그래프
INF = int(1e9)
dis = [[INF]*(n+1) for _ in range(n+1)]

# 자기자신은 0
for i in range(1,n+1):
    for j in range(1, n+1):
        if i == j:
            dis[i][j] = 0



for _ in range(m):
    a, b, c = map(int, input().split())

    if dis[a][b] > c:
        dis[a][b] = c


# 와샬~

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j] = min(dis[i][j] , dis[i][k] + dis[k][j])


# print

for i in range(1,n+1):
    for j in range(1,n+1):
        print(dis[i][j], end = " ")
    print("")