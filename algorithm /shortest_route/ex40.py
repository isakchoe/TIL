import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

distance = [INF]*(n+1)

data = [[] for _ in range(n+1)]


for i in range(m):
    a,b = map(int, input().split())

    data[a].append((b,1))
    data[b].append((a,1))


def dij(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dis, now = heapq.heappop(q)

        if distance[now] < dis:
            continue

        for i in data[now]:
            cost = i[1] + dis

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))


dij(1)

count = 1
max_result = 0
max_index = 0
for i in range(1,n+1):
    if distance[i] > max_result:
        max_result = distance[i]
        max_index = i
        count = 1
    elif distance[i] == max_result:
        count +=1
#
# for i in range(1,n+1):
#     if distance[i] == max_result:
#         count +=1



print(max_index, max_result, count)

