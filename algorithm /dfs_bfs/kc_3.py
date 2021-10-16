
from _collections import deque


def main(passenger, train):

    # 역 개수 == 노드 개수
    n = len(passenger)

    # 인접리스트 만들기
    data = [[] for _ in range(n+1)]

    for edge in train:
        a, b = edge
        data[a].append(b)

    # 방문 체크이자, 거리 변수.
    distance = [-1]*(n+1)

    q = deque()
    q.append([passenger[0],1])
    distance[1] = passenger[0]

    while q:
        dis, now = q.popleft()

        for next in data[now]:
            # 방문한적 없으면 방문하고 거리 갱신
            if distance[next] == -1:
                distance[next] = dis + passenger[next-1]
                q.append([distance[next], next])

    answer = [0,0]

    for i in range(1,n+1):
        if distance[i] == max(distance):
            answer[0] = i
            answer[1] = distance[i]

    print(answer)


passenger = [2,1,2,2]
train = [ [1,2], [1,3], [2,4]]

main(passenger,train)
