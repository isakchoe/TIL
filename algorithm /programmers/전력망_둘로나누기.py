

def find_p(parent, x):
    if parent[x] != x:
        parent[x] = find_p(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    p_a = find_p(parent, a)
    p_b = find_p(parent, b)

    if p_a > p_b:
        parent[p_a] = p_b
    else:
        parent[p_b] = p_a


def solution(n, wires):

    answer = float('inf')

    for i in range(len(wires)):
        new_list = wires[0:i] + wires[i+1:]

        #  부모 테이블 세팅
        parent = [0]*(n+1)
        for idx in range(1,n+1):
            parent[idx] = idx

        # 유니언 연산
        for a, b in new_list:
            union(parent, a, b)

        # 유니언 업데이트!!
        # for e in range(1, len(parent)):
        #     parent[e] = find_p(parent, e)
        dic = {}
        for index in range(1, len(parent)):
            if find_p(parent, index) not in dic:
                dic[find_p(parent, index)] = 1
            else:
                dic[find_p(parent, index)] += 1

        result_list = list(dic.values())

        result = abs(result_list[0] - result_list[1])
        answer = min(answer, result)
    return answer




n = 4
wires = [[1,3], [2,4], [3,4]]
print(solution(n, wires))


