from _collections import deque

def solution(people, limit):
    # 최대 2명 탑승, limit 아래
    # people 정렬, 최소 최대 합이 limit 이하 만족하는 최대값으로 구성
    # 배 출발하면 count ++ , 새로운 배 (빈 스택 생성)
    # 끝까지 탐색하면서 위 과정 반복

    # 정렬
    people.sort()
    p = deque()

    for i in people:
        p.append(i)
    # 구명보트
    stack = []
    total = 0

    while p:
        if len(stack) == 0:
            stack.append(p.popleft())
            total += 1
        else:
            left = limit - stack[-1]
            while p:
                if p[-1] <= left:
                    p.pop()
                    # 보트출발
                    stack.pop()
                    break
                else:
                    # 혼자 타야하는 사람들!
                    p.pop()
                    total += 1
    return total