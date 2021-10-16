def solution(n, words):
    #     딕셔너리 이용
    # 제일 먼저 중복되는 인덱스 확인
    #  그 인덱스 사람 확인
    # 예외처리, 없으면 [0,0]
    # 끝말잇기 규칙 위배!!

    dic = {}
    dic[words[0]] = 1
    index = -1
    for i in range(1, len(words)):
        #         처음 단어이고, 끝말잇기 조건 만족
        if words[i] not in dic and words[i][0] == words[i - 1][-1]:
            dic[words[i]] = 1
        else:
            index = i + 1
            break

        #     예외
    if index == -1:
        return [0, 0]
    else:
        #         a : 차례, B: 번호
        a = index // n + 1
        b = index % n
        if b == 0:
            b = n
            a -= 1

        return [b, a]
