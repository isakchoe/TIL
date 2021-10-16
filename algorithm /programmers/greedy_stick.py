

def solution(name):

    # 커서이동 먼저:    앞 Vs 뒤   최소한의 방향으로 이동
    # 문자 수정: A 문자에서 시작 ==> target 까지 거리 비교   앞 vs 뒤
    # 매번 조이스틱 누를때마다 count ++
    # 탐색 끝나면 count 리턴

    n = len(name)

    # 알파벳
    up = {"B": 1, "C" : 2, "D" :3 ,"E" : 4 , "F" : 5, "G": 6, "H": 7, "I": 8, "J" : 9, "K": 10, "L": 11, "M":12 }
    down = {"Z" : 1, "Y": 2, "X": 3, "W": 4, "V": 5, "U": 6, "T" : 7, "S": 8, "R":9, "Q":10, "P": 11, "O": 12, "N": 13}

    # 커서위치
    now = 0
    # 정답
    count = 0

    index_list = []

    # 수정할 인덱스 삽입
    for i in range(n):
        if name[i] != "A":
            index_list.append(i)


    #  순차 탐색하면 안된다.. 수정할 인덱스들 중에서 매번 가장 가까운 위치의 인덱스를 먼저 수정!!
    while len(index_list) > 0:

        # 임시 이동거리
        temp = 21
        # 다음 수정할 인덱스
        next = 0

        # now 로부터 가장 가까운 인덱스랑, 해당 인덱스까지 거리 구하기
        for i in range(len(index_list)):
            index = index_list[i]
            left = now +n -index
            right = abs(index - now)

            # 좌우 비교
            small = min(left,right)

            # 최소이면 갱신
            if small < temp:
                temp = small
                next = index

        # 카운트 ++, now 갱신
        count += temp
        now = next
        # 수정한 인덱스는 대기 리스트에서 삭제
        index_list.remove(next)

        #문자수정
        target = name[next]

        #  a부터 m까지는 up!, 나머지는 down!
        if target in up:
            count += up[target]
        else:
            count += down[target]

    return count