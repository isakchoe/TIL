
from collections import deque


def solution(numbers, target):

    q = deque()

#     총합, 횟수
    q.append([0,0])

    answer = 0

    while q:
        total, times = q.popleft()

        # 횟수가 개수보다 크면 성립하지 않음
        if times > len(numbers):
            break
        # 전체 개수 전부다 계산한 경우, 타겟 적중할때
        if times == len(numbers) and total == target:
            answer += 1
        # 아직 계산이 끝나지 않은 경우, 플마 동시 수행
        elif times < len(numbers):
            q.append([total + numbers[times], times + 1])
            q.append([total - numbers[times], times + 1])

    return answer


