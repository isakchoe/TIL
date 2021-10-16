

import heapq


def solution(scoville, K):

    # 힙큐에서 두개씩 빼고 계산 ==> count++ ,  그리고 다시 넣기 ==> 확인! ==> 반복

    q = []

    # 힙에 삽입
    for i in scoville:
        heapq.heappush(q, i)


    answer = 0


    # 확인 단계
    while len(q) > 1 :
        first = heapq.heappop(q)

        # 확인
        if first >= K:
            return answer

        if len(q) == 0:
            break

        sec = heapq.heappop(q)

        # mix
        temp = first + (2 * sec)
        answer += 1
        heapq.heappush(q,temp)




    return -1