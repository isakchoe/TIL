
from collections import deque


def solution(priorities, location):

    q = deque()

    for i in range(len(priorities)):
        q.append([i, priorities[i]])

    # 최대값
    max_value = max(priorities)

    count = 1

    while q:
        index, now  = q.popleft()

        # 최대가 아니면 다시 뒤로
        if now != max_value:
            q.append([index, now])
        else:
            # 프린트 하고자 하는 문서면 카운트 return
            if index == location:
                return count
            else:
                # 아니면, 출력하고 리스트에서 삭제
                priorities.remove(max_value)
                # 최대값 , 카운트 갱신
                max_value = max(priorities)
                count += 1


    return answer