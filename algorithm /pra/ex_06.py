
#
# def solution(food_times, k):
#     answer = 0
#
#     if sum(food_times) < k:
#         return -1
#     time = 0
#
#     while time <= k:
#         for i in range(len(food_times)):
#
#             if food_times[i] != 0:
#                 if time == k:
#                     answer = i + 1
#                     break
#
#                 food_times[i] -= 1
#                 time += 1
#
#         if answer != 0:
#             break
#
#     return answer

import heapq

def solution(food_times, k):

    # 시간내에 모두 다 먹는 경우
    if sum(food_times) <= k:
        return -1

    q = []

    # 우선순위큐 삽입
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i +1))

    sub_total = 0

    # 이전 음식 시간
    pre = 0
    # 남은 음식 개수
    length = len(food_times)

    while sub_total + (q[0][0]-pre)* length <= k:

        # 제일 소요시간이 작은 음식부터 빼기,
        now = heapq.heappop(q)[0]
        sub_total += (now-pre) * (length)

        # 완료한 음식은 개수에서 빼기, 완료 음식 pre 처리
        length -= 1
        pre = now

    q.sort(key=lambda x : x[1])

    return q[(k-sub_total)%length][1]





















