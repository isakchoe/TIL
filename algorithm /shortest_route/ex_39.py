import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dij():
    q = []
    heapq.heappush(q, (data[0][0],0,0))
    distance[0][0] = data[0][0]

    dx =[0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        dis, r,c  = heapq.heappop(q)

        if distance[r][c] < dis:
            continue
        for i in range(4):
            nr = r +dx[i]
            nc = c+ dy[i]

            if nr<0 or nr>=n or nc<0 or nc>=n:
                continue

            cost = dis + data[nr][nc]

            if distance[nr][nc] > cost:
                distance[nr][nc] = cost
                heapq.heappush(q, (cost, nr,nc))


t = int(input())

for tc in range(t):

    n = int(input())

    distance = [[INF] *n for _ in range(n)]

    data = []

    for i in range(n):
        temp = list(map(int, input().split()))
        data.append(temp)

    dij()

    print(distance[n-1][n-1])




