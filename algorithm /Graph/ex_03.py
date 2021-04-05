


def find_p(p, x):
    if p[x] != x:
        p[x] = find_p(p, p[x])
    return p[x]

def union(p, a, b):
    a = find_p(p,a)
    b = find_p(p, b)

    if a < b:
        p[b] = a
    else:
        p[a] = b




n, m = map(int, input().split())

p = [0]*(n+1)

for i in range(1, n+1):
    p[i] = i

edges = []
max_result = 0
total = 0

for _ in range(m):
    a ,b ,c = map(int, input().split())
    edges.append((c,a,b))

# sort

edges.sort()

for edge in edges:

    cost, a, b = edge

    if find_p(p, a) != find_p(p, b):
        union(p,a,b)
        total += cost

        if max_result < cost:
            max_result = cost

print(total - max_result)

