
def find_parent(p, x):
    if p[x] != x :
        p[x] = find_parent(p, p[x])

    return p[x]


def union(p, a, b):
    a = find_parent(p,a)
    b = find_parent(p,b)

    if a < b:
        p[b] = a
    else:
        p[a] = b


def main():

    n, m = map(int, input().split())

    # 부모노드 테이블
    p = [0] * (n+1)
    # 초기값 세팅
    for i in range(n+1):
        p[i] = i



    for _ in range(m):
        c, a, b = map(int, input().split())

        if c == 0:
            union(p, a, b)

        if c == 1:
            result_a = find_parent(p, a)
            result_b = find_parent(p, b)

            if result_a == result_b :
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    main()
