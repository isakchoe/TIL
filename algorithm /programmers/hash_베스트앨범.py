

def solution(genres, plays):
    # 장르 탐색하면서 딕셔너리 만들기  키: 장르, 값: 리스트  ==> (재생횟수, 인덱스)
    # 딕셔너리2 : 키: 장르. 값: 총합  ==> 내림차순 정렬 ==>
    # 딕셔너리2 바탕으로 장르별 탐색하면서 0,1번째 인덱스 리스트에 넣기
    # 리스트 리턴!!

    dic = {}
    dic2 = {}

    # 장르 탐색
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = plays[i]
        else:
            dic[genres[i]] += plays[i]

        if genres[i] not in dic2:
            dic2[genres[i]] = [(plays[i],i)]
        else:
            dic2[genres[i]].append((plays[i], i))
            # 내림차순 정렬, 번호 낮은거 먼저
            dic2[genres[i]].sort(key= lambda x:(-x[0], x[1]))

    # dic 정렬
    dic = sorted(dic.items(), key= lambda x : x[1] , reverse= True)

    answer = []

    for i in range(len(dic)):
        now = dic[i][0]
        if len(dic2[now]) >=2:
            answer.append(dic2[now][0][1])
            answer.append(dic2[now][1][1])
        else:
            answer.append(dic2[now][0][1])

    return answer

