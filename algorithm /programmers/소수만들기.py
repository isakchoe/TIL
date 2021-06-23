
from itertools import combinations
import math

def is_prime(num):

    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num) ) +1):
        if num %i == 0:
            return False
    return True


def solution(nums):
    #     조합 이용
    #     합 구하기 ==> 소수 판별
    #   소수이면 answer ++

    answer = 0

    #     조합
    combi = list(combinations(nums ,3))
    #     map ==> 합
    combi = list(map(sum, combi))
    print(combi)

    #     탐색하면서 소수 확인
    for i in combi:
        if is_prime(i):
            answer += 1

    return answer