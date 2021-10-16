
# 유니언 파인드 활용

import sys
input = sys.stdin.readline


def find_p(parent,x):
    if parent[x] != x:
        # 이걸 실수했네
        # 기본 서로소 알고리즘
        # return find_p(parent,parent[x])

        # 개선된 서로소 알고리즘
        parent[x] = find_p(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_p(parent, a)
    b = find_p(parent, b)

    if a>b:
        parent[a] = b
    else:
        parent[b] = a




# 입력
n = int(input())
m = int(input())

# 부모계수
parent = [0]*(n+1)

# 초기화
for i in range(1,n+1):
    parent[i] = i


total= n

for _ in range(m):
    x, y = map(int,input().split())

    # x부터 y 까지 통합
    for i in range(x,y):
        # 연결 안되어있으면, 벽 부수기
        if find_p(parent,i) != find_p(parent,i+1):
            union(parent,i,i+1)
            total -= 1


# 순회, 최신화  ,, 굳이 필요 없는듯  ==> 유니언 파인드 이용해서 개수셀때는 최신화 필요,
for i in range(1,n+1):
    find_p(parent,i)


dic = {}
count = 0
for i in range(1,n+1):
    if parent[i] not in dic:
        dic[parent[i]] = 1
        count+=1



#  이 부분 때문에 게속 틀림,   ==> 유니언 파인드 함수가 잘못되어서 틀림
# temp = set(parent[1:])
# print(len(list(temp)))

# 출력
print(total, parent)



