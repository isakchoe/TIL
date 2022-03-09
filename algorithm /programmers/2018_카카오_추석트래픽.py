
def makeTime(time_arr):

    a = int(time_arr[0])*3600*1000
    b = int(time_arr[1])*60*1000
    c = float(time_arr[2])*1000

    return a+b+c



def solution(lines):

    start_time = []
    end_time = []


    for line in lines:
        temp = line.split(' ')
        time = temp[1]
        run_time = float(temp[2][:-1])

        time_splited = time.split(':')

        # 시간 parse, 변환
        time_sec = makeTime(time_splited)

        start_time.append(time_sec)
        end_time.append(time_sec + run_time)


    answer = 0

    total = start_time + end_time


    # start 를 기준으로. 1초 범위 선정해서 중복 계산하기 //
    # end 를 기준으로 1초 범위 선정해서 중복 계산
    for i in range(len(start_time)):
        start = start_time[i]
        end = end_time[i]
        count = 0
        for j in range(len(end_time)):
            if end_time[j] >= start and start_time[j]<= start+1000:
                count += 1

            elif end_time[j] >= end and  start_time[j] <= end + 1000 :
                count += 1

        answer = max(answer, count)

    return answer


