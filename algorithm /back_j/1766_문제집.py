

import heapq


# 위상정렬 문제
# 진입차수 같으면, 번호 작은거 먼저 출력  ==> 우선순위큐를 이용했다
# 보통 위상정렬은 큐를 사용하는데, 이문제는 우선순위큐를 이용하는 것이 핵심


# 입력
n, m = map(int, input().split())

# 인접차수
indegree = [0]*(n+1)

# 인접리스트
ad_list = [[] for _ in range(n+1)]

# 간선정보
for _ in range(m):
    a, b = map(int, input().split())
    ad_list[a].append(b)

    indegree[b] += 1


q = []
# 진입차수 0인거 삽입
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

answer = []

while q:
    now = heapq.heappop(q)
    answer.append(now)
    # 간선 제거
    for next in ad_list[now]:
        indegree[next] -= 1

        if indegree[next] == 0:
            heapq.heappush(q, next)

for i in answer:
    print(i, end = " ")