def solution(tickets):

    dic = {}

    # 출발지를 key 로 딕셔너리 생성
    for depart, desti in tickets:
        if depart not in dic:
            dic[depart] = [desti]

        else:
            dic[depart].append(desti)

    # 목적지를 알파벳 내림차순 순으로 정렬 : 스택은 반대이기에!
    for k in dic.keys():
        dic[k].sort(reverse=True)

    answer = []

    # 스택
    s = ['ICN']

    while s:
        now = s[-1]
        # now 출발지가 없거나, 티켓을 사용한 경우 --> 여행경로 종료!! 마지막이라는 뜻 --> 따라서 answer에 삽입, pop
        if now not in dic or len(dic[now]) == 0:
            answer.append(s.pop())
        else:
            # 있는경우, 해당경로 스택에 올리고 방문 처리
            s.append(dic[now].pop())

    answer.reverse()

    return answer