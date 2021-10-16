
# 신장트리 거리구하기--> BFS
# 카카오커머스랑 같은 문제
# 백준에 같은 문제 여러개 존재

from collections import deque

# 압력
n,m = map(int, input().split())

# 인접리스트
ad_list = [[] for _ in range(n+1)]

# 간선 입력 받기
for _ in range(n-1):
    a, b, distance = map(int, input().split())

    ad_list[a].append([b,distance])
    ad_list[b].append([a,distance])

# bfs 함수
def bfs(start, end):
    q =deque()
    visited = [False] * (n + 1)

    #    방문처리, 초기 큐 세팅
    visited[start] = True

    for node, cost in ad_list[start]:
        visited[node] = True
        q.append([node,cost])

    while q:
        now, cost = q.popleft()
        # 범위 확인
        if now == end:
            return cost
        else:
            for node, dis in ad_list[now]:
                # 방문여부 확인
                if visited[node] == False:
                    # 방문처리
                    visited[node] = True
                    # 삽입
                   q.append([node, dis + cost])


# 출력
for _ in range(m):
    a,b = map(int, input().split())
    print(bfs(a,b))