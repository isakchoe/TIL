

t = int(input())

for num in range(t):
    k, n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    # 기름양
    total = k
    # 기름 충전횟수
    count = 0

    for i in range(1, len(arr)):
        # 충전할 지점
        if total < arr[i] and total >= arr[i-1]:
            count += 1
            total = arr[i-1] + k

    # 마지막 조정
    if total < n:
        if total >= arr[-1]:
            if arr[-1] + k >= n:
                count += 1
        else:
            count = 0

    print(f"#{num+1} {count}")

