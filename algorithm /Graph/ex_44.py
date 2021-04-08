
n = int(input())


x_list = []
y_list = []
z_list = []

# x, y, z 값 받기
for i in range(n):
    x, y, z = map(int, input().split())

    x_list.append(x)
    y_list.append(y)
    z_list.append(z)

# 정렬
x_list.sort()
y_list.sort()
z_list.sort()

total_list = []

for i in range(n-1):

    # x, y, z 각각의 거리를 구해서 삽입 --> 거리, a, b 노드 번호
    total_list.append((x_list[i+1] - x_list[i], i, i+1))
    total_list.append((y_list[i + 1] - y_list[i], i, i + 1))
    total_list.append((z_list[i + 1] - z_list[i], i, i + 1))

# 정렬
total_list.sort()

parent = [0]*(n)

for i in range(n):
    parent[i] = i


def find_p(p, x):
    if p[x] != x:
        p[x] = find_p(p, p[x])
    return p[x]

def union(p,a,b):
    a = find_p(p,a)
    b = find_p(p,b)

    if a > b:
        p[a] = b
    else:
        p[b] = a

result = 0

for edge in total_list:
    # 비용, a노드, b노드
    cost, a, b = edge

    # 연결되어 있지 않으면 연결!
    if find_p(parent,a) != find_p(parent,b):
        union(parent, a, b)
        result += cost

print(result)