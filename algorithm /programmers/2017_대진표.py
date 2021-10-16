
import math

def solution(n ,a ,b):
    #     n 로그 2 만큼 반복!!
    #   A 짝수면 다음 라운드 반타작, 홀수면 +1 하고 반타작
    #  작은 숫자가 홀수여야 만난다!!

    answer = 0
    for i in range(1, int(math.log2(n)) +1):
        m = min(a, b)
        max_team = max(a, b)

        #         만나는경우
        if max_team - m == 1 and m % 2 != 0:
            answer = i
            break
        else:
            if a % 2 == 0:
                a = a // 2
            else:
                a = a // 2 + 1
            if b % 2 == 0:
                b = b // 2
            else:
                b = b // 2 + 1

    return answer
