
from _collections import deque

n, m ,k ,x = map(int, input().split())

# 인접리스트 만들기
data = [[] for _ in range(n+1)]

# 연결 입력 받기
for i in range(m):
    a,b = map(int,input().split())
    data[a].append(b)

# 방문 체크 리스트
visited = [False] *(n+1)

q = deque()
q.append([0,x])

visited[x] = True

result = []

while q:
    distance, now = q.popleft()

    # 거리가 k가 맞다면 삽입하고 스킵
    if distance == k:
        result.append(now)
        continue

    # 연결된 노드들 확인
    for node in data[now]:
        # 방문하지 않았다면 방문!, 큐에 삽입
        if not visited[node]:
            q.append([distance+1, node])
            visited[node] = True
# 정렬
result.sort()

# 출력

if len(result) == 0:
    print(-1)

for i in result:
    print(i)

