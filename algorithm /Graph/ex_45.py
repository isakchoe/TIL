from _collections import deque

# 테이스 케이스
t = int(input())

for tc in range(t):

    # 노드 개수
    n = int(input())

    # 작년 순위
    last = list(map(int, input().split()))

    # 바뀐 성적 쌍
    m = int(input())

    indegree = [0] * (n+1)

    graph = [ [False] *(n+1) for _ in range(n+1)]

    # 인접 행렬, 인접 차수  만들기
    for i in range(n):
        for j in range(i+1, n ):
            graph[last[i]][last[j]] = True
            indegree[last[j]] += 1


    # 인접 관계 스위칭하기
    for i in range(m):
        x, y = map(int, input().split())
        # x -> y 관계
        if graph[x][y]:
            graph[x][y] = False
            graph[y][x] = True

            indegree[x] += 1
            indegree[y] -= 1
        else:
            graph[x][y] = True
            graph[y][x] = False
            indegree[x] -= 1
            indegree[y] += 1


    q = deque()

    # 인접차수 0인것 큐에 넣기
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)


    result = []

    cycle = False
    miss = False

    # !!! 중요!! 딱 n 번만 큐를 돌린다.  while 사용하지 않는다
    for i in range(n):
        # 사이클 발생하는 경우
        if len(q) == 0:
            cycle = True
            break
        # 순위 알 수 없는 경우
        if len(q) == 2:
            miss = True
            break

        now = q.popleft()

        result.append(now)

        for j in range(1,n+1):
            if graph[now][j]:
                indegree[j] -= 1

                # 진입차수 0 이면 삽입
                if indegree[j] == 0:
                    q.append(j)




    # 결과 출력
    if cycle:
        print("IMPOSSIBLE")
    elif miss :
        print("?")

    else:
        for i in result:
            print(i, end = " ")
        # 개행!
        print()










