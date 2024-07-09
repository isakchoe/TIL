def solution(edges):
    # 1,2,3
    #  진입 차수 0인거 찾자
    # 진입 차수 = 0  -> 막대모양 시작 or 새로운 정점
    # 진입 차수 =0 and 나가는 방향 2개이상...

    # 1. 새 정점 찾기
    #  진입 차수 2개, 나가는거 2개... == 3유형...
    # 2. 새 정점 기준으로.... 탐색?

    s_dic = {}
    e_dic = {}

    for edge in edges:
        start, end = edge

        if start not in s_dic:
            s_dic[start] = 1
        else:
            s_dic[start] += 1

        if end not in e_dic:
            e_dic[end] = 1
        else:
            e_dic[end] += 1

    temp = []
    for k, v in s_dic.items():
        if v >= 2:
            temp.append(k)

    # 새로운 정점 찾기...
    new_node = 0
    for i in temp:
        if i not in e_dic:
            new_node = i

    

solution(edges=[[2, 3], [4, 3], [1, 1], [2, 1]])