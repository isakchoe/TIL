

import heapq

def djk(start, end, n, ad_list):

    # 거리 리스트
    INF = int(1e9)
    distance = [INF]*(n+1)

    # 우선순위큐 세팅
    q = []
    heapq.heappush(q, [0,start])
    distance[start] = 0

    while q:
        cost, now = heapq.heappop(q)

        if distance[now] > cost:
            continue

        for node, fare in ad_list[now]:
            new_cost = cost + fare

            if distance[node] > new_cost:
                distance[node] = new_cost
                heapq.heappush(q, [new_cost, node])

    return distance[end]


def solution(n, s, a, b, fares):

    ad_list = [ [] for _ in range(n+1)]

    # 인전리스트 세팅
    for fare in fares:
        x,y,z = fare

        ad_list[x].append([y,z])
        ad_list[y].append([x,z])


    answer = djk(s,a,n,ad_list) + djk(s, b, n, ad_list)

    for i in range(1,n+1):
        # i지점까지 합승한뒤 각자 택시 타고 집으로
        temp = djk(s, i, n, ad_list)  + djk(i, a, n, ad_list) + djk(i, b, n, ad_list)

        if temp < answer:
            answer = temp

    return answer
