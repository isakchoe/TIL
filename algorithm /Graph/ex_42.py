

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

parent = [0]* (g+1)

for i in range(g+1):
    parent[i] = i

for i in range(p):
    plane.append(int(input()))

result = 0

for gate in plane:
    if find_parent(parent, gate) != 0 :
        union(parent, gate, gate -1)
        result += 1

print(result)









