
def solution(clothes):

    blank = []

    # 키값으로 부위별 개수 파악
    dic = {}

    for i in range(len(clothes)):
        if clothes[i][1] not in dic:
            dic[clothes[i][1]] = 1
            blank.append(clothes[i][1])
        else:
            dic[clothes[i][1]] += 1

    answer = 1
    # 계산
    for i in range(len(blank)):
        # 종류별 옷개수 + 1(안입는경우)
        temp = dic[blank[i]] + 1
        answer *= temp

    return answer -1