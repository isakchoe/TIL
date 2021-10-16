

# 유니온-파인드 서로소 집합 문제


def find(p,a):
    if p[a] != a:
        p[a] = find(p, p[a])
    return p[a]

def union(p,a,b):
    a = p[a]
    b = p[b]

    if a > b:
        p[a] = b
    else:
        p[b] = a

def main():
    n, m = map(int, input().split())

    parent = [0] *(n+1)

    for i in range(1,n+1):
        parent[i] = i

    for i in range(1,n+1):
        temp = list(map(int, input().split()))

        for e in range(n):
            if temp[e] == 1 :
                union(parent, i, e+1)

    plan = list(map(int, input().split()))

    p = parent[plan[0]]

    for i in range(len(plan)):
        if parent[plan[i]] != p:
            print("NO")
            break
        if i == len(plan) -1 and parent[plan[i]] == p:
            print("YES")








main()