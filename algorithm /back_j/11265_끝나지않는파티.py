
# 다익스트라!
# 넘버링 맞추기

import heapq

def djk(start, end, time):

    q = []
    # 비용, 노드
    heapq.heappush(q, [0, start])

    INF = int(1e9)
    distance = [INF] * (n + 1)

    distance[start] = 0

    while q:
        cost, now = heapq.heappop(q)

        if distance[now] < cost:
            continue

        for node in ad_list[now]:
            new_node, new_cost = node

            if distance[new_node] > cost + new_cost:
                distance[new_node] = cost + new_cost
                heapq.heappush(q, [cost + new_cost, new_node])


    if distance[end] <= time:
        print("Enjoy other party")
    else:
        print("Stay here")



n, m = map(int, input().split())
ad_list = [[] for _ in range(n+1)]

# ad_list 세팅
for i in range(1,n+1):
    arr = list(map(int, input().split()))

    for j in range(n):
        if j+1 != i:
            ad_list[i].append([j+1, arr[j]])


# 출력
for _ in range(m):
    a,b,c = map(int, input().split())
    djk(a,b,c)
