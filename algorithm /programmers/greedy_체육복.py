
def solution(n, lost, reserve):
    answer = n

    #여벌옷 가져온자 lost 확인.. !! 먼저 처리해야 한다!! 문제 조건 잘 읽고 우선순위 확인하기!
    for num in lost:
        if num in reserve:
            reserve.remove(num)
            lost.remove(num)

    # lost 탐색
    for num in lost:
        pre = num -1
        next = num + 1

        if pre in reserve:
            reserve.remove(pre)
        elif next in reserve:
            reserve.remove(next)
        else:
            answer -= 1

    return answer