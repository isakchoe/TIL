
import math

def solution(brown, yellow):
    answer = []

    total = brown + yellow

    for i in range(3, int(math.sqrt(total))+1):
        m = i
        n = total//i

        if n*m == total:
            if 2*(n+m) - 4 == brown:
                answer.append(n)
                answer.append(m)
                break

    return answer