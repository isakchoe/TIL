


def dfs(row, now_result, n):
    global result

    # 끝까지 다 돌았어
    if row == n:
        result = max(result, now_result)
        return

    # 백트래킹!!
    if now_result <= result:
        return

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            dfs(row+1, now_result * matrix[row][i]*(0.01), n)
            visited[i] = False



t = int(input())

for tc in range(1,t+1):
    n = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(n)]
    result = 0

    visited = [False]*n

    dfs(0, 1, n)

    result = '{:.6f}'.format(result*100)
    print(f'#{tc} {result}')
