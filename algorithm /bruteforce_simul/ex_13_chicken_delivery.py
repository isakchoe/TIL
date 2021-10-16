

from itertools import combinations

n,m = map(int, input().split())


chick_lsit = []
house_list = []

# 행렬 입력 받기
for i in range(n):
    temp = list(map(int, input().split()))

    for e in range(n):
        if temp[e] == 1:
            house_list.append([i,e])
        if temp[e] == 2:
            chick_lsit.append([i,e])


# 치킨집 조합 경우의 수
combi_list = list(combinations(chick_lsit,m))




# 도시의 치킨 거리 구하기 함수
def distance(house, chick):
    total = 0

    for h_r, h_c in house :
        # 집에서 치킨집 거리 구하기
        result = int(1e9)

        # 모든 치킨집 거리 구해서, 최소값 찾기
        for r,c in chick:
            result = min(abs(r-h_r) + abs(c-h_c), result)
        # 최소값 total에 더하기
        total += result
    return total


answer = int(1e9)

# 모든 치킨집 조합 거리 구해보기
for i in range(len(combi_list)):
    answer = min(distance(house_list, combi_list[i]), answer)

print(answer)