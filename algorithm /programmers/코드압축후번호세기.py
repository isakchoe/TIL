
# 재귀 --> 2021 하반기 라인 문제랑 비슷

def make(arr):
    global zero
    global one

    temp_sum = 0
    # 쿼드 압축 가능한지 합으로 판별
    for i in range(len(arr)):
        temp_sum += sum(arr[i])

    # 쿼드 압출 불가능
    if temp_sum != 0 and temp_sum != (len(arr) * len(arr)):

        n = len(arr) // 2
        # 재귀 종료 조건.
        if n == 1:
            result = sum(arr[0]) + sum(arr[1])
            one += result
            zero += 4 - result
            return

        one_divi = []
        two_divi = []
        three_divi = []
        four_divi = []

        # 여기서 디버깅 오래걸림 --> row를 for문 돌려야한다.
        # 1,2,3,4 사분면 재귀
        for i in range(n):
            one_divi.append(arr[i][0:n])
            two_divi.append(arr[i][n:])
        for i in range(n, len(arr)):
            three_divi.append(arr[i][:n])
            four_divi.append(arr[i][n:])

        make(one_divi)
        make(two_divi)
        make(three_divi)
        make(four_divi)
    # 쿼드압축 가능
    else:
        if temp_sum == 0:
            zero += 1
        else:
            one += 1


zero = 0
one = 0

def solution(arr):
    make(arr)
    return [zero, one]








