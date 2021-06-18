

def solution(record):
    # 구현 문제!!
    # enter, leave, change 순서대로 작성
    # change 이름만 바꿔줄것!! 아이디 기준으로!!
    # 해쉬 이용!!

    dic = {}
    result = []
    # 탐색
    for s in record:
        temp = list(s.split())
        # id, 상태
        id = temp[1]
        state = temp[0]

        #입장
        if state =="Enter":
            result.append([id,"님이 들어왔습니다."])
            # 닉네임 변경 혹은 초기화
            dic[id] = temp[2]
        #퇴장
        elif state == "Leave":
            result.append([id, "님이 나갔습니다."])
        # change
        elif state == "Change":
            # 닉네임 변경
            dic[id] = temp[2]

    answer = []

    for i in range(len(result)):
        id = result[i][0]
        str = dic[id] + result[i][1]

        answer.append(str)

    return answer
