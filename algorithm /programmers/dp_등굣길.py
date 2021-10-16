#
# import heapq
#
# def solution(m, n, puddles):
#
#     # 다익스트라 ==> 종착지 종착할때마다 카운트 ++ 카운트 리턴, 재방문 처리 ==> 같아도 방문
#
#     INF = int(1e9)
#
#     # 그래프 만들기
#     graph = [[INF]*m for _ in range(n)]
#
#     # 침수 지역
#     for r,c in puddles :
#         graph[c-1][r-1] = -1
#
#
#
#     # 다익스트라~
#     q = []
#     # 거리, row, col
#     graph[0][0] = 0
#     heapq.heappush(q,(0,0,0))
#
#
#     dx = [1,0]
#     dy = [0,1]
#
#     count = 0
#
#     while q:
#         now, r, c = heapq.heappop(q)
#
#         # 도달하면 카운트 업
#         if r == n-1 and c == m- 1:
#             count += 1
#             continue
#
#         if graph[r][c] < now:
#             continue
#
#         for i in range(2):
#             nr = r + dx[i]
#             nc = c + dy[i]
#
#             if  0<= nr < n and 0<=nc < m:
#                 if graph[nr][nc] != -1:
#                     cost = now + 1
#                     # 같아도 방문!
#                     if graph[nr][nc] > cost:
#                         graph[nr][nc] = cost
#                         heapq.heappush(q, (cost, nr,nc))
#
#     return count%1000000007


def solution(m, n, puddles):

    # 그래프
    graph = [[1]*m for _ in range(n)]

    # 웅덩이
    for x,y in puddles:
        graph[y-1][x-1] = 0


#     1행, 1열 웅덩이 뒤에는 갈 수 없다!!

    # 0행 처리
    for i in range(len(graph[0])-1):
        #  그 뒤는 전부 0
        if graph[0][i] == 0:
            graph[0][i+1] = 0

    # 0열 처리
    for i in range(len(graph)-1):
        if graph[i][0] == 0 :
            graph[i+1][0] = 0

    # 점화식
    for i in range(1,n):
        for j in range(1, m):
            # 웅덩이가 아닐경우!
            if graph[i][j] != 0:
                graph[i][j] = graph[i-1][j] + graph[i][j-1]


    return graph[n-1][m-1]%1000000007





