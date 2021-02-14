
from collections import deque

n, m, k ,x = map(int, input().split())



# 2차원 데이터!!,,, 하지만 항상 배열로 생각하지 말것!!,  연결 상태가 아닌 연결 노드를 그대로 저장
data = [[] for _ in range(n+1)]



for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)


# 거리값 저장 변수 만들기!!!

distance = [-1]*(n+1)

distance[x] = 0

q = deque([x])

while q:

    v = q.popleft()

    for next_node in data[v]:
        if distance[next_node] == -1:
            distance[next_node] = distance[v] + 1

            q.append(next_node)


index = 1

for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        index +=1

if index == 1:
    print(-1)











