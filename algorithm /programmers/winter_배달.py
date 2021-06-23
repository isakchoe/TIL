
import heapq


def solution(N, road, K):
    #     다익스트라
    #     k 보다 작거나 같은경우만 count ++

    INF = int(1e9)
    distance = [INF ] *( N +1)

    #     연결 리스트
    ad_list = [[] for _ in range( N +1)]

    for a ,b ,c in road:
        ad_list[a].append([b ,c])
        ad_list[b].append([a ,c])

    #     삽입
    distance[1] = 0

    q = []
    heapq.heappush(q, [0, 1])

    # 큐 돌리기
    while q:
        cost, now = heapq.heappop(q)

        if distance[now] < cost:
            continue

        for to, dis in ad_list[now]:
            new_cost = dis + cost
            if distance[to] > new_cost:
                distance[to] = new_cost
                heapq.heappush(q ,[new_cost, to])

    # 정답 출력
    answer = 0
    for i in range(1 ,len(distance)):
        if distance[i] <= K:
            answer += 1

    return answer