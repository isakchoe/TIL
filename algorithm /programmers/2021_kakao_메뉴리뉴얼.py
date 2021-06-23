
from itertools import combinations

def solution(orders, course):
    #     course 개수마다 조합뽑기 ==>
    #   dic 에 저장하여 개수 파악
    #   최대값 삽입, ==> 여러개면 같이 삽입
    #   오름차순 정렬

    # 예외 !! ==> 2개이상이어야 한다!!!

    answer = []
    for c in course:
        dic = {}
        # 탐색
        for i in orders:
            # 조합
            if len(i) >= c:
                combi = list(combinations(i,c))
            else:
                continue

            for j in range(len(combi)):
                a = sorted(combi[j])
                temp = "".join(a)
                if temp not in dic:
                    dic[temp] = 1
                else:
                    dic[temp] += 1
        # print(dic)

        # 가장큰 value 찾기

        #  손님이 주문한 가지수보다 많은 코스인경우, 스킵
        if len(dic) == 0:
            continue
        max_result = max(dic.values())
        # 최소 2개이상 조건!!
        if max_result < 2:
            continue

        for key, num in dic.items():
            if num == max_result:
                answer.append(key)

    # 오름차순 정렬
    answer.sort()
    return answer




# 해쉬!!   ==> items, keys()  valuese ,,, max 값!!
# 조합
#  문자열!! ==> join
# sort 와 sorted 의 차이