
INF = int(1e9)

def main():

    n,m = map(int, input().split())

    data = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for e in range(1,n+1):
            if i == e:
                data[i][e] = 0

    # 거리가 아닌 관계!
    for i in range(m):
        a, b = map(int, input().split())
        data[a][b] = 2
        data[b][a] = -2



    for x in range(1, n + 1):
        for y in range(1, n + 1):
            for z in range(1, n + 1):
                # 이것이 포인트! 
                if (data[y][x] < 0 and data[x][z] <0) or (data[y][x] >0 and data[x][z] >0):

                    data[y][z] = min(data[y][z], data[y][x] + data[x][z])

                else:
                    continue



    count = n

    for i in range(1,n+1):
        for e in range(1,n+1):
            if data[i][e] == INF:
                count = count - 1
                break

    print(count)


main()
