
def solution(targets):
    min_x = 100000000
    max_x = 0

    for start, end in targets:
        if min_x < start:
            min_x = start
        if max_x > end:
            max_x = end

    # 누적 리스트
    arr = [0] * (max_x - min_x + 1)

    for start, end in targets:
        arr[start] += 1
        arr[end] -= 1

