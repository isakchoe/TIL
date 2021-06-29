
def solution(info, query):

    # 효율성 제로!!
    answer = []

    # 질문 탐색하면서
    for q in query:
        count = 0
        temp = q.split()
        #  조건 담기
        blank = []

        lang = temp[0]
        if lang != "-":
            blank.append(lang)
        job = temp[2]
        if job !="-":
            blank.append(job)
        exp = temp[4]
        if exp !="-":
            blank.append(exp)
        food = temp[6]
        if food !="-":
            blank.append(food)
        score = int(temp[7])

        # 지원자 탐색
        for i in info:
            parse = i.split()
            c = 0
            # 조건 모두 만족하는지 확인
            for j in range(len(blank)):
                if blank[j] not in parse:
                    c += 1
                    break
            # 모두 만족하면 스코어 확인
            if c == 0:
                if int(parse[-1]) >= score:
                    count += 1
            else:
                continue
        
        answer.append(count)

    return answer



