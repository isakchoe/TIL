



from collections import deque

# 처음에 큐에 넣을때만 정렬해서 넣으면 된다.


# 입력받기
n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
# 좌표 - 인덱스 불일치
s, x, y =  map(int, input().split())


# 처음 큐에 넣기
q = deque()

temp = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            # 감염번호, row, col, 시간
            temp.append([matrix[i][j], i,j,0])

# 정렬
temp.sort(key=lambda x:x[0])

# 큐에 넣기
for i in temp:
    q.append(i)


answer = 0

while q:
    virus_num, row, col, sec = q.popleft()

    # 원하는 조건이면,좌표 정보는 완전 일치해야하며, 시간은 딱맞거나 이하거나
    if sec <= s and row == x-1 and col == y-1:
        answer = matrix[row][col]
        break

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(4):
        nr = row +dx[i]
        nc = col +dy[i]

        if 0<=nr<n and 0<=nc<n:
            # 빈공간일경우 확산
            if matrix[nr][nc] == 0:
                matrix[nr][nc] = virus_num
                q.append([matrix[nr][nc], nr, nc, sec + 1])

print(answer)

