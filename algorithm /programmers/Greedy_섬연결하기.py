

def find_p(p,a):
    if p[a] != a:
        p[a] = find_p(p,p[a])
    return p[a]

def uni(p,a,b):
    a = find_p(p,a)
    b = find_p(p,b)

    if a>b:
        p[a] = b
    else:
        p[b] = a


def solution(n, costs):

    # 크루스칼 알고리즘
    # 유니언, 파인드 구현
    # cost 오름차순 정리
    # 연결 하면서 cost 증가, 리턴!

    # 루트 테이블 생성
    parent = [0]*n
    # 자기자신으로 세팅
    for i in range(n):
        parent[i] = i

    # cost 비용순으로 정렬
    costs.sort(key = lambda  x: x[2])

    total = 0

    # 연결
    for i in range(len(costs)):
        a = costs[i][0]
        b = costs[i][1]
        cost = costs[i][2]

        if find_p(parent,a) != find_p(parent, b):
            uni(parent,a,b)
            total += cost

    return total
