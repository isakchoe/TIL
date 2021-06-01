
import heapq

def solution(operations):

    # 최소힙
    q = []
    # 최대힙
    m_q = []
    # 큐의 길이
    count = 0


    # 명령 순서에 따라 처리

    for c in operations:

        # 큐 비우기
        if count == 0:
            while q:
                heapq.heappop(q)
            while m_q:
                heapq.heappop(m_q)
        #숫자 삽입
        if c[0] == "I":
            count += 1
            temp = ""
            for i in range(2,len(c)):
                temp += c[i]
            # 삽입
            heapq.heappush(q, int(temp))
            heapq.heappush(m_q, -int(temp))

        #최소값 삭제
        elif c[0] == "D":

            # 큐가 비어있으면 무시
            if count == 0:
                continue

            count -= 1

            if c[2] == "-":
                heapq.heappop(q)
            # 최대값 삭제
            else:
                heapq.heappop(m_q)


    # 큐가 비어있으면 0,0

    if count == 0 :
        return [0,0]
    # 아니면 최대, 최소
    else:
        a = heapq.heappop(q)
        b = heapq.heappop(m_q)

        if a == -b:
            return

        return [-b, a]

# def solution(operations):
#
#     blank = []
#
#     for c in operations:
#         if c[0] == "I":
#             temp = ""
#             for i in range(2,len(c)):
#                 temp += c[i]
#
#             blank.append(int(temp))
#
#         elif c[0] == "D":
#
#             if len(blank) == 0:
#                 continue
#
#             # 최소값 삭제
#             if c[2] =="-":
#                 heapq.heapify(blank)
#                 heapq.heappop(blank)
#                 # 다시 리스트로
#                 blank = list(blank)
#
#             else:
#                 blank.sort()
#                 blank.pop()
#
#
#     if len(blank) == 0:
#         return  [0,0]
#     else:
#         blank.sort()
#         return [blank[-1], blank[0]]




print(solution(operations=["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))