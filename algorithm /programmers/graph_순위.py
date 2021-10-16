

def solution(n, results):

    answer = 0

    INF = int(1e9)

    # 그래프
    graph = [[INF]*(n+1) for _ in range(n+1)]

    # 간선 관계 입력받기

    for a, b in results:
        # 이긴경우 1
        graph[a][b] = 1
        # 진경우 -1
        graph[b][a] = -1


    # 플로이드 워샬~
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                # 핵심! 같은 관계일때만 연결
                if (graph[i][k] > 0 and graph[k][j] > 0) or (graph[i][k] <0 and graph[k][j] < 0):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])



    # 탐색하면서 모든행이 연결되어 있으면 카운트 ++
    for i in range(1,n+1):
        count = 0
        for j in range(1,n+1):
            # 자기자신 빼고 연결 되어있으면 카운트 ++
            if graph[i][j] != INF and i != j:
                count += 1
        # 자기자신빼고 모두 연결 되어있으면 answer ++
        if count == n-1:
            answer += 1


    return  answer
