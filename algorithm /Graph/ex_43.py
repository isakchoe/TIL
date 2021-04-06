
n, m = map(int, input().split())

p = [0] * n

for i in range(n):
    p[i] = i

edges = []


for _ in range(m):
    x,y,z = map(int, input().split())
    edges.append((z,x,y))

edges.sort()


def find(p,x):
    if p[x] != x:
        p[x] = find(p,p[x])
    return p[x]

def union(p, a,b):
    a = find(p,a)
    b = find(p,b)

    if a > b:
        p[a] = b
    else:
        p[b] = a


result = 0

for edge in edges:
    cost, x, y = edge

    if find(p,x) != find(p, y):
        union(p,x,y)

    else:
        result += cost

print(result)
