

def solution(jobs):

    # 들어온 시간 순서로 정렬
    jobs.sort()

    answer = 0
    n = len(jobs)
    # 시간
    time = 0

    # SJF => 시간 제일 적게 걸리는 놈 선택,  완료시간 - 들어온시간 ++ answer 마지막에 answer n으로 평균내기

#     첫번째 실행
    answer += jobs[0][1]
    time += jobs[0][0] + jobs[0][1]
    jobs.remove(jobs[0])

    while len(jobs) >0:
        temp = 1000
        index = 0
        for i in range(len(jobs)):
            # 대기중인 프로세스들
            if jobs[i][0] <= time:
                # 제일 짧은거 먼저 하기
                if jobs[i][1] < temp:
                    temp = jobs[i][1]
                    index = i

        # 대기중인 프로세스가 없는경우
        if jobs[index][0] > time:
            time = jobs[index][0] + jobs[index][1]
            answer += time - jobs[index][0]
        # 대기중인 프로세스가 있는 경우
        else:
            time += jobs[index][1]
            answer += time - jobs[index][0]
        # 완료한거 삭제
        jobs.remove(jobs[index])

    return answer//n





