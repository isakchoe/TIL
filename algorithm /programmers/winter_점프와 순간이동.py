
def solution(n):
    # 순간이동 == 현재 온거리 * 2
    # k 만큼 점프

    #  n  이 짝수면 이분탐색 ==>
    #  홀수면 -1 하고 이분탐색  count ++

    count = 0

    while n >1:
            # 쩍슈
        if n%2 == 0:
            n = n//2
        else:
            n -= 1
            count += 1
    count += 1
    return count