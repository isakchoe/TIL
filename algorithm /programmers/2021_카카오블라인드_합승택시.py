



# 1. 합승 x a, b 각자 다익 합 구하기
# 2.  모든 노드까지 합승하고, 내린다음 각자 집가는 경우의 수 구하기
# 3. 1과2 비교해서 최소 리턴

# 플로이드워셜 이용



def solution(n, s, a, b, fares):
    INF = int(1e9)
    data = [[INF] * (n+1) for _ in range(n+1)]
    # 자기 자신까지 거리는 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i ==j:
                data[i][j] =0
    # 인접행렬 세팅
    for fare in fares:
        x,y,c = fare
        data[x][y] = c
        data[y][x] = c
    # 워셜
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                data[i][j] = min(data[i][j], data[i][k] + data[k][j])
    # 2. 모든 경우의 수 탐색
    answer = data[s][a] + data[s][b]
    for i in range(1,n+1):
        # i 지점까지 합승하고, 그 이후 각자 택시
        temp = data[s][i] + data[i][a] + data[i][b]
        if temp < answer:
            answer = temp
    return answer



