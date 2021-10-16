

# 입력받기
n,m = map(int, input().split())
rice = list(map(int, input().split()))

# 정렬
rice.sort()

# 높이 최대값
h = rice[-1] - 1

def bi(arr, target, start, end):

    answer = 0

    while start <= end:
        mid = (start + end)//2

        total = 0

        # 자른 떡 길이 계산
        for i in rice:
            if i > mid:
                total += i - mid


        if total < target:
            end = mid - 1

        if total >= target:
            start = mid + 1
            answer = mid

    return mid

# 이진탐색 수행
result = bi(rice, m, 0, h )

print(result)
