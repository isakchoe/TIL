def solution(d, budget):
    #     그리디 유형
    #     작은거부터 주면 된다
    #     오름차순 정렬 ==> 탐색 하면서 마이너스

    d.sort()

    answer = 0

    for i in d:
        if budget >= i:
            answer += 1
            budget -= i
        else:
            break
    return answer
