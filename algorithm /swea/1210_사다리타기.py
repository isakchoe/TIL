

from collections import deque

for tc in range(1,11):
    n = int(input())
    # 행렬 입력받기
    data = []
    for _ in range(100):
        data.append(list(map(int,input().split())))

    # 도착지점 index
    end = 0
    for j in range(100):
        if data[99][j] == 2:
            end = j


    # 끝에서 올라가기

    # 동,서,북   '남'은 없다. 내려가지 않으니깐
    dr = [0,0,-1]
    dc = [1,-1,0]

    # deque 이용
    q = deque()

    # 초기 세팅
    q.append([99,end])
    data[99][end] = 0

    answer = 0

    while q:
        row, col = q.popleft()

        # 시작점 도착
        if row == 0:
            answer = col
            break

        for i in range(3):
            new_row = row + dr[i]
            new_col = col + dc[i]

            # 범위
            if 0<=new_row < 100 and 0<=new_col <100:
                # 조건: 갈수 있는 방향
                if data[new_row][new_col] == 1:
                    # 방문처리
                    data[new_row][new_col] = 0
                    # 큐에 삽입
                    q.append([new_row,new_col])

                    break

    # 출력
    print(f'#{tc} {answer}')