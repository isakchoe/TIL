
# 입력받기
n = int(input())
home = list(map(int, input().split()))

# 정렬
home.sort()

# 중간 인덱스에 설립
mid = len(home)//2

total = 0
sub_total = 0

for i in range(len(home)):
    total += abs(home[mid] - home[i])
    sub_total += abs(home[mid-1] - home[i])

# 합 비교, 출력
if total > sub_total:
    print(home[mid])
else:
    print(home[mid-1])