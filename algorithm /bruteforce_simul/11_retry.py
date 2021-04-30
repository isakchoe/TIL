
# 입력받기
n = int(input())
k = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]

# 사괴 위치는 1
for i in range(k):
    a,b = map(int, input().split())
    graph[a][b] = 1

l = int(input())

turn = []

for i in range(l):
    x,y = input().split()
    turn.append((int(x),y))

# 뱀 정보

snake = [(1,1)]

dir = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
time = 0

while True:

    head_r, head_c = snake[-1]

    # 회전 시간 확인
    for i in range(len(turn)):
        sec, to = turn[i]
        # 회전하는 경우
        if time == sec:
            if to == "L":
                dir = (dir + 3)%4
            else:
                dir = (dir + 1)%4
            break

    # 다음 방향
    next_r = head_r + dx[dir]
    next_c = head_c + dy[dir]

    # 몸 충돌 하는 경우
    if (next_r, next_c) in snake:
        time += 1
        break

    # 정상 범위
    if 1<=next_c<=n and 1<=next_r<=n:
        snake.append((next_r, next_c))

        # 사과 안먹은 경우
        if graph[next_r][next_c] != 1:
            snake.pop(0)
        time += 1
        continue

    # 범위 벗어나는 경우
    else:
        time += 1
        break


print(time)
