from collections import deque


def check(a, b):
    length = len(a)

    total = 0
    for i in range(length):
        if a[i] != b[i]:
            total += 1

    if total == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    q = deque()

    q.append([0, begin])

    answer = 0

    while q:

        # 변환 횟수, 현재 값
        num, now = q.popleft()

        # 타켓 적중하면 횟수 리턴
        if now == target:
            return num

        # 한개만 다른 단어 찾기, 그리고 지우기
        for word in words:
            if check(now, word):
                q.append([num + 1, word])
                words.remove(word)

    return answer