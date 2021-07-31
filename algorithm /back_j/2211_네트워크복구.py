


#
# # 크루스칼 , 최소신장트리
#
# def find_p(parent,x):
#     if parent[x] != x:
#         return find_p(parent,parent[x])
#     return x
#
# def union(a,b):
#     a = find_p(parent,a)
#     b = find_p(parent, b)
#
#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a
#
# # 입력받기
# n, m = map(int, input().split())
# nodes = []
# for _ in range(m):
#     a,b,c = map(int,input().split())
#     nodes.append([a,b,c])
#
# # 부모
# parent = [0]*(n+1)
# for i in range(1,n+1):
#     parent[i] = i
#
# # 비용 최소 순으로 정렬
# nodes.sort(key = lambda  x: x[2])
#
#
# fix_list = []
#
# for node in nodes:
#     a, b, cost = node
#     # 연결 안되어 있으면 연결
#     if find_p(parent,a) != find_p(parent,b):
#         union(a,b)
#         fix_list.append([a,b])
#
# print(len(fix_list))
# for a, b in fix_list:
#     print(a,b)


import sys
input = sys.stdin.readline

import heapq


# 다익 버전

# 입력
n, m = map(int, input().split())
INF = int(1e9)

# 거리
distance = [INF]*(n+1)

# 인접리스트
ad_list = [[] for _ in range(n+1)]

# path_dic
path =  {i:0 for i in range(1,n+1)}

# 삽입
for _ in range(m):
    a, b, c = map(int, input().split())

    ad_list[a].append([b,c])
    ad_list[b].append([a,c])


# 초기 세팅
distance[1] = 0
q = []
heapq.heappush(q,[0,1])



while q:
    # 비용, 노드
    cost, now = heapq.heappop(q)

    if distance[now] < cost:
        continue

    # 노드, 비용
    for node, c in ad_list[now]:
        new_cost = c + cost
        if distance[node] > new_cost:
            distance[node] = new_cost
            heapq.heappush(q, [new_cost, node])
            path[node] = now


print(n-1)

for i in range(2, n+1):
    print(i, path[i])




