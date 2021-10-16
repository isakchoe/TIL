
from bisect import bisect_left, bisect_right

# 입력받기
n,m = map(int, input().split())
num = list(map(int, input().split()))

right = bisect_right(num, m)
left = bisect_left(num, m)


if right == left:
    print(-1)

else:
    print(right - left)
