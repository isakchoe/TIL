

from itertools import combinations


def check(arr,relation):
    dic = {}

    # 튜플 --> 리스트
    arr = list(arr)

    for row in relation:
        temp = ""
        for index in arr:
            temp += row[index]
        if temp in dic:
            return False
        else:
            dic[temp] = 1
    return True


def solution(relation):
    #  모든조합구하기
    #  유일성 검사 --> 함수로 처리
    #  최소성 검사 --> in 으로 처리
    #  answer = [ '1', '23' 문자열 형식으로 하기!!  ]

    col = len(relation[0])

    answers = []

    for i in range(1, col+1):
        #  i 개 뽑는 경우의 수
        combi = list(combinations(list(range(0,col)),i ))


        for arr in combi:
            # 유일성 검사
            if check(arr, relation):
                # 최소성 검사: arr 의 부분집합이 answers에 없어야 한다.
                pivot = 0
                for answer in answers:
                    # answer 가 arr의 부분집합이면, 최소성 성립 x
                    if set(answer) == set(answer).intersection(set(arr)):
                        pivot += 1
                        break
                if pivot == 0 :
                    answers.append(arr)

    return len(answers)


