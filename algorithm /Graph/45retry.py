
from _collections import deque



t = int(input())

for _ in range(t):

    n = int(input())
    last = list(map(int, input().split()))
    m = int(input())

    change = []

    for i in range(m):
        a,b = map(int, input().split())
        change.append((a,b))


        #진입차수
    indegree = [0]*(n+1)

    ad_list = [[] for _ in range(n+1)]




    # 진입차수, 인접 리스트 세팅
    for i in range(n):
        indegree[last[i]] = i
        for j in range(i+1, n):
            ad_list[last[i]].append(last[j])


    # 올해 순서 변경
    for i in range(m):
        a, b = change[i]
        print(indegree[a], indegree[b])
        if indegree[a] > indegree[b]:
            print("a")
            ad_list[b].remove(a)
            ad_list[a].append(b)

        else:
            print("b")
            ad_list[a].remove(b)
            ad_list[b].append(a)


    # 인접차수 갱신

    new_indegree = [0]*(n+1)

    for i in range(1,n+1):
        for j in ad_list[i]:
            new_indegree[j] += 1





    q = deque()



    for i in range(1,n+1):
        if new_indegree[i] == 0:
            q.append(i)

    if len(q) == 0:
        print("IMPOSSIBLE")
        break


    result = []

    while n >0 :
        now = q.popleft()

        result.append(now)

        for node in ad_list[now]:
            new_indegree[node] -= 1

            if new_indegree[node] == 0:
                q.append(node)

        n-=1

    if len(q) == 0:
        for i in result:
            print(i, end =" ")
        print()

    else:
        print("?")


