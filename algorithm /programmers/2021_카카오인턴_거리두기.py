
# bfs
#  p 인 경우만 탐색
# 동서남북 있으면 바로 false
#  대각선,,, 있으면, 그에 따른 칸막이 여부 확인 체크

from collections import deque

def bfs(q, matrix):

    dx = [0 ,0 ,1 ,-1]
    dy = [1 ,-1 ,0 ,0]

    dx2 = [0 ,0 ,2 ,-2]
    dy2 = [2 ,-2 ,0 ,0]

    dx3 = [1 ,1 ,-1 ,-1]
    dy3 = [1 ,-1 ,-1 ,1]


    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r +dx[i]
            nc = c + dy[i]
            #     바로 옆
            if 0 <= nr < 5 and 0 <= nc < 5:
                if matrix[nr][nc] == "P":
                    return False

        # 2칸
        for i in range(4):
            nr = r + dx2[i]
            nc = c + dy2[i]

            if 0 <= nr < 5 and 0 <= nc < 5:
                if matrix[nr][nc] == "P":
                    if matrix[(nr + r) // 2][(nc + c) // 2] != "X":
                        return False
        # 대각선
        for i in range(4):
            nr = r + dx3[i]
            nc = c + dy3[i]

            if 0 <= nr < 5 and 0 <= nc < 5:
                if matrix[nr][nc] == "P":
                    if matrix[nr][c] != "X" or matrix[r][nc] != "X":
                        return False

    return True


def solution(places):
    answer = []

    for place in places:
        q = deque()

        for i, row in enumerate(place):
            for j in range(5):
                if row[j] == "P":
                    q.append([i, j])

        result = bfs(q, place)
        if result:
            answer.append(1)
        else:
            answer.append(0)

    return answer