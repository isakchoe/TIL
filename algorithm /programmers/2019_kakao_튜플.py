
def solution(s):
    # s 파싱
    blank = []
    temp = []
    st = ""


    # parsing!!  쉽고 빠르고 정확!!
    s1 = s.lstrip('{').rstrip('}').split('},{')
    print(s1)

    # 어렵고 부정확
    for i in range(1 ,len(s ) -1):
        # 시작 '{'
        if s[i] == "{":
            temp = []
        #   '}'   ==>  이전 숫자 temp 에 삽입, temp 를  blank에 삽입, st 초기화
        elif s[i] == "}":
            temp.append(int(st))
            blank.append(temp)
            st = ""
        #  콤마 1.중간 2. 배열 중간
        elif s[i] == ",":
            if s[i -1] == "}":
                continue
            else:
                temp.append(int(st))
                st = ""
        else:
            st += s[i]

    # sort
    blank.sort(key = lambda x: len(x))

    # 정답 배열
    answer = []

    for i in range(len(blank)):
        for j in range(len(blank[i])):
            if blank[i][j] not in answer:
                answer.append(blank[i][j])

    return answer

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

if __name__ == '__main__':
    print(solution(s))