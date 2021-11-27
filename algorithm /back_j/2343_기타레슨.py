
# 입력받기
m,n = map(int, input().split())
lessons = list(map(int, input().split()))

# 블루레이 용량의 최소, 최대
left = max(lessons)
right = sum(lessons)

total = right

count = 0
answer = int(1e9)

while left <= right:

    # 블루레이 크기
    mid = (left+right)//2

    # 블루레이 개수
    count = 0
    temp = 0

    # 전체 블루레이 개수 구하기
    for i in range(len(lessons)):
        if temp + lessons[i] > mid:
            count += 1
            temp = 0

        temp += lessons[i]

    count += 1

    # 블루레이 크기 늘려야 한다.
    if count > n:
        left = mid + 1

    # 크기 줄여야 한다.
    elif count <= n:
        right = mid - 1
        # 개수가 맞는 경우, 그 범위 내에서 최대값 찾기
        if count == n:
            answer = min(mid, answer)


# 가장 핵심!, mid 가 아니라 left 출력 
print(left)




