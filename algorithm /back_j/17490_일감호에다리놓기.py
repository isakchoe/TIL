
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))


# 다리 건설 필요없는 경우. (예외 케이스 잘 생각하기!! )
if m <= 1:
    print("YES")
    exit()


check = [0]*n

for _ in range(m):
    a, b = map(int, input().split())
    check[b-1] = 1



total = 0

# 시작, 끝 찾기
start, end = 0, 0

for i in range(n):
    if check[i] == 1:
        start = i
        break

for i in range(n-1, -1, -1):
    if check[i] == 1:
        end = i
        break


temp_min = nums[start]

for i in range(start+1, end+1):
    # 새로운 슬라이스
    if check[i] == 1:
        total += temp_min
        temp_min = nums[i]

    else:
        if nums[i] < temp_min:
            temp_min = nums[i]


# start, end 4가지 경우의 수
if start != 0 and end != n-1:
    temp_min2 = min(nums[0:start])
    temp_min2 = min(temp_min2, min(nums[end:]))

elif start !=0 and end == n-1:
    temp_min2 = min(nums[0:start])
    total += nums[end]

elif start==0 and end == n-1:
    temp_min2 = nums[end]

elif start ==0 and end != n-1:
    temp_min2 = min(nums[end:])


total += temp_min2


if total > k:
    print("NO")
else:
    print("YES")

