
import math
# 입력

n, a, b, c, d = map(int, input().split())

# !!1개당 가격 구해서 싼곳에서 최대한 사기

# 1개당 가격
per_a = b/a
per_c = d/c

# 총 비용
total = 0

# c에서 사기
if per_a > per_c:
    # 최대한 많이 사기
    total += n//c * d

    # 남은 사야할 꽃
    rest = n%c


    # 남은거 어디서 사? 첫번째, 두번째 가게 구입비용 비교
    if d > (math.ceil(rest/a)) * b:
        total += math.ceil(rest/a) * b
    else:
        total += d


# 첫번째가 더 싼 경우
else:
    total += n//a * b

    rest = n%a

    if b > (math.ceil(rest/c)) * d:
        total += math.ceil(rest/c) * d
    else:
        total += b


print(total)