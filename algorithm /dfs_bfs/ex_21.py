from _collections import deque

n, l ,r = map(int, input().split())

data = []

for i in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)



def bfs( x, y, index):


    q = deque()

    q.append([x,y])


    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    union_list = []

    union_list.append([x,y])

    num = 1
    total = data[x][y]

    while q:

        row, col = q.popleft()

        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]

            if nx >=0 and nx <n  and ny>=0 and ny< n:

                t1 = data[row][col]
                t2 = data[nx][ny]

                diff = abs(t1-t2)

                # 조건 만족해도 방문한적 없어야 한다!!
                if diff >=l and diff <=r and union[nx][ny] == -1 :
                    union_list.append([nx,ny])
                    union[nx][ny] = index

                    q.append([nx,ny])
                    num += 1
                    total += data[nx][ny]


    for i,j in union_list:
        data[i][j] = total//num

    return num




total_count = 0
while True:
    index = 0

    union = [[-1] * n for _ in range(n)]

    for i in range(n):
        for e in range(n):
            if union[i][e] == -1:
                bfs(i,e,index)
                index += 1


    if index == n*n :
        break
    total_count += 1


print(total_count)






