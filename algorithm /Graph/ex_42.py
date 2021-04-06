

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a =find_parent(parent,a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


g = int(input())
p = int(input())

plane = []

for i in range(p):
    plane.append(int(input()))

plane.sort()

parent = [0] *(g+p+1)

for i in range(1,g+p+1):
    parent[i] = i


result = 0

# plane 노드



print(result)








