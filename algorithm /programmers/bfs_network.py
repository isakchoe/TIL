def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]


def union(p, a, b):
    a = find(p, a)
    b = find(p, b)

    if a > b:
        p[a] = b
    else:
        p[b] = a


def solution(n, computers):
    parent = [0] * (n)

    for i in range(n):
        parent[i] = i

    answer = n

    for node in range(len(computers)):
        for i in range(n):
            if computers[node][i] == 1 and node != i:
                if find(parent, node) != find(parent, i):
                    union(parent, node, i)
                    answer -= 1

    return answer