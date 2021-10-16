import heapq


def solution(n, edge):
    INF = int(1e9)

    # 거리 변수
    distance = [INF] * (n + 1)
    # 인접 리스트
    graph = [[] for i in range(n + 1)]

    for i in edge:
        x, y = i

        graph[x].append(y)
        graph[y].append(x)

    # 다익스트라 알고리즘
    def dj(start):
        q = []
        distance[start] = 0

        heapq.heappush(q, [distance[start], start])

        while q:
            dis, now = heapq.heappop(q)

            if distance[now] < dis:
                continue

            for i in graph[now]:
                cost = dis + 1
                if distance[i] > cost:
                    distance[i] = cost
                    heapq.heappush(q, [cost, i])

    dj(1)

    max_result = -1
    total = 0
    for i in range(1, n + 1):
        if distance[i] > max_result:
            max_result = distance[i]

    # 최대값 개수 구하기
    for i in range(1, n + 1):
        if distance[i] == max_result:
            total += 1

    return total