
from _collections import deque



n = int(input())

# 인접 차수
indegree = [0]*(n+1)

# 인정 리스트
ad_list = [[] for _ in range(n+1)]

# 과목당 수강 시간
time_list = [0]*(n+1)

# 선수과목 포함 완료 시간
total_time = [0]*(n+1)

# 인접 리스트, 인접 차수 세팅
for i in range(n):
    temp = list(map(int, input().split()))
    time_list[i+1] = temp[0]

    # 간선 연결
    for j in range(1, len(temp)-1):
        ad_list[temp[j]].append(i+1)
        indegree[i+1] += 1


q = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        # i+1 번까지 누적 수강시간과, 현재 인덱스
        q.append((time_list[i], i))
        total_time[i] = time_list[i]


while q:

    ac_time, now = q.popleft()

    # 간선 제거
    for node in ad_list[now]:
        indegree[node] -= 1

        if indegree[node] == 0:
            # 핵심 포인트!!!... 기존의 시간보다 크다면 갱신
            if total_time[node] < ac_time + time_list[node]:
                # 삽입
                q.append((ac_time +time_list[node], node))
                # total 갱신
                total_time[node] = ac_time + time_list[node]



# 출력

for i in range(1,n+1):
    print(total_time[i])






