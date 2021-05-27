

def solution(participant, completion):


    dic = {}

    # 참가자 딕셔너리 만들기, 동명이인 주의!!
    for i in range(len(participant)):
        if participant[i] not in dic:
            dic[participant[i]] = 1
        else:
            dic[participant[i]] += 1

    # 완주자 딕셔너리에서 값 빼기
    for i in range(len(completion)):
        if completion[i] in dic:
            dic[completion[i]] -= 1

    # dic 에서 0값이 아니면, 미완주자
    for i in range(len(participant)):
        if dic[participant[i]] != 0:
            return participant[i]
