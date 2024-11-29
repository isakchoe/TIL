from itertools import product
import heapq
import copy

def solution(k, n, reqs):
    #  경우의 수 -> 시간 초과 안되는지.. 판단... 수학...
    #  경우의 수 제대로 수식 세우기...
    range_values = range(n + 1-k)
    combinations = product(range_values, repeat= k)
    result = [tuple(x+1 for x in combo) for combo in combinations if sum(combo) == n-k]

    INF = 1e9
    answer = INF
    for r in result:
        wait_time = calculate(r, reqs)
        answer = min(answer, wait_time)
    return answer


def calculate(mento, reqs):
    answer = 0
    queues = [0]

    for _ in range(len(mento)):
        temp = []
        heapq.heapify(temp)
        queues.append(copy.deepcopy(temp))

    for start_time, cost_time, type in reqs:
        q = queues[type]

        # 멘토 자리 남는 경우
        if len(q) < mento[type-1]:
            heapq.heappush(q, start_time + cost_time)
            continue

        fast_end_time = heapq.heappop(q)

        # waiting
        if start_time < fast_end_time:
            heapq.heappush(q, fast_end_time + cost_time)
            wait_time = fast_end_time - start_time
            answer += wait_time
        else:
            heapq.heappush(q, start_time + cost_time)
    return answer

k = 2
n = 3
regs = [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]
print(solution(k,n,regs))