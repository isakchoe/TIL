# import heapq
#
# def solution(n, times):
# #     우선순위 큐 이용!
# #     pop 할때마다 n 감소, 시간 플러스 하고 다시 큐에 삽입
# #   과정 반복,,,
#
#
#     q= []
#
#     for i in range(len(times)):
#         heapq.heappush(q, [times[i], i])
#
#
#     while True:
#
#         # 가장 빠른 검문소, 인덱스
#         now, index  = heapq.heappush(q)
#
#         n -= 1
#
#         if n == 0:
#             return now
#
#         # 검문 완료 시간
#         next = now + times[index]
#
#         # 삽입
#         heapq.heappush(q,[next, index])
#

def solution(n, times):

    times.sort()

    start = 0
    end = n * times[0]

    while start <= end:
        mid = (start+end)//2

        total = 0

        for i in times:
            if i >= mid:
                total += mid//i

        if total >= n:
            end = mid - 1

        elif total < n:
            start = mid + 1




