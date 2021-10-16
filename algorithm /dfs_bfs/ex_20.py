
from itertools import  combinations
from _collections import deque

# 입력값 처리
n = int(input())
data = []

for i in range(n):
    temp = list(input().split())
    data.append(temp)

# 학생수 구하기
s_num = 0
for i in range(n):
    for e in range(n):
        if data[i][e] == "S":
            s_num += 1



# bfs 함수
def bfs(arr):

    length = len(arr)
    q = deque()

    check_list =[]

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    # 큐에 교사 위치 삽입
    for i in range(length):
        for e in range(length):
            if arr[i][e] =="T":
                q.append([i,e])
                check_list.append([i,e])


    while q:

        row, col = q.popleft()

        for i in range(4):

            nx = row + dx[i]
            ny = col + dy[i]

            while nx >=0 and ny>=0 and nx <length and ny<length:

                if arr[nx][ny] != "O":
                    arr[nx][ny] = "T"

                if arr[nx][ny] == "O":
                    break

                nx = nx + dx[i]
                ny = ny + dy[i]


    answer = 0

    # 안걸린 학생수 구하기
    for i in range(length):
        for e in range(length):
            if arr[i][e] == "S":
                answer += 1


    return answer



# 기둥을 세우고 체크하는 메인 함수

def check_main(data):

    blank = []

    n = len(data)

    temp = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if data[i][j] == "X":
                blank.append([i, j])

    choice = list(combinations(blank, 3))

    for i in choice:

        for a in range(n):
            for b in range(n):
                temp[a][b] = data[a][b]

        for loca in i:
            temp[loca[0]][loca[1]] = "O"

        student = bfs(temp)

        if student == s_num:

            return "YES"


    return "NO"


print(check_main(data))











