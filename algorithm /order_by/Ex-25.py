def solution(N, stages):
    answer = []

    total_users = len(stages)

    # 계수정렬 활용
    count = [0] * (N + 2)

    for i in range(len(stages)):
        count[stages[i]] += 1

    blank = []

    # 0번째 인덱스는 필요없으니깐, 1부터 ,,, 마지막 인덱스는 all clear 이니깐 무시
    for i in range(1, len(count) - 1):
        if count[i] == 0:
            blank.append([i, 0])
        else:
            total = 0
            # 해당 스테이지 이상인  사람 수 구하기,, all clear 한 사람도 포함!!
            for e in range(i, len(count)):
                total += count[e]

            rate = count[i] / total
            blank.append([i, rate])



    blank.sort(key=lambda x: (-x[1], x[0]))

    for i in range(len(blank)):
        answer.append(blank[i][0])

    return answer