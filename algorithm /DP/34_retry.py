
# 입력받기
n = int(input())
data = list(map(int, input().split()))

# dp[i] == i+1 번부터 끝까지 최대값일때, 열외 병사 수
dp = [-1] * n
dp[n-1] = 0

# 최대값, 내리차순 가장 큰 값
max_value = data[-1]
recent = data[-1]


# 거꾸로 탐색,
for i in range(n-2, -1, -1):
    # 가장 이전보다 크면, 내림차순에 문제 없음.
    if data[i] > recent:
        dp[i] = dp[i+1]
        # 최근값 현져값으로 갱신, 최대값에 현재값 더하기
        recent = data[i]
        max_value += data[i]

    else:
        # 현재 인덱스 포함한 내림차순 vs 포함하지 않는 내림차순 비교

        temp_total = data[i]
        start = data[i]
        count = 0
        # 현재 인덱스부터 끝까지 탐색
        for j in range(i+1, n):
            # 내림차순이면 더하기
            if start > data[j]:

                temp_total += data[j]
                start = data[j]
            # 아니면 열외 카운트 up
            else:
                count += 1


        # 비교, 현재 인덱스포함 내림차순이 더 크면, dp[i] = 카운트 최근값, 토톨값 갱신
        if temp_total > max_value:
            dp[i] = count
            recent = data[i]
            max_value = temp_total
        else:
            #  현재값 포함하지 않는 내림차순이 더 크면, 현재값을 열외!! ==> +1 해줘야 한다.
            dp[i] = dp[i+1] + 1

# 출력
print(dp[0])