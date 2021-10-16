from itertools import permutations
import math

# 소수판별 함수
def is_prime(num):
    if num == 1 or num == 0:
        return False

    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False

    return True


def solution(numbers):

    temp = []
    blank = []

    #     numbers 문자열 쪼개기
    for i in range(len(numbers)):
        temp.append(numbers[i])

    #     1개부터 n개 까지 순열 구하기
    for i in range(1, len(numbers) + 1):
        result = list(permutations(temp, i))

        for e in range(len(result)):
            target = ''
            for s in range(i):
                target += result[e][s]

            if is_prime(int(target)) and int(target) not in blank:
                blank.append(int(target))

    answer = len(blank)

    return answer