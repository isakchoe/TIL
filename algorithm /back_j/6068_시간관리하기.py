
n =int(input())

arr = []
for _ in range(n):
    t, s = map(int, input().split())
    arr.append([t,s])

# 마감시간 급한거 부터 순차정렬
arr.sort(key=lambda x:x[1])

start_time = arr[0][1] - arr[0][0]

answer =  -1

for time in range(start_time, -1, -1):
    temp = time

    pivot = 0
    for during_time, deadline in arr:
        temp += during_time

        # 마감여부 확인
        if temp > deadline:
            pivot += 1
            break

    # 모든 조건 만족
    if pivot == 0:
        answer = time
        break


print(answer)


