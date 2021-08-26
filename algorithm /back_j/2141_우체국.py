

# 이분탐색
import sys
input = sys.stdin.readline


n = int(input())

# 마을 번호만 담기
arr = []

# 마을정보
dic ={}

# 전체인구수
number_of_people = 0

for i in range(n):
    # 마을별 사람 수 만큼, 채워 넣기
    a,b = map(int, input().split())

    # 딕셔너리로 처리
    dic[a] = b
    # 마을 번호 담기
    arr.append(a)
    # 전체 인구수 더하기
    number_of_people += b

# 마을 순서 정렬
arr.sort()


half = number_of_people//2

# 정확히 중간 안 나눠질 때, 비교
if number_of_people%2 == 0:

    # 두 지점이 같은 마을이라면 상관없다:

    # half 벤치마킹
    total = 0
    answer = 0

    for i in arr:
        temp = dic[i]
        total += temp

        if total > half:
            answer = i
            break

    total_cost = 0

    for i in arr:
        total_cost += dic[i] *(abs(answer - i))

    # half -1 벤치마킹
    total_back = 0
    answer_back = 0

    for i in arr:
        temp = dic[i]
        total_back += temp

        if total_back > half-1:
            answer_back = i
            break

    total_cost_back = 0

    for i in arr:
        total_cost_back += dic[i] * (abs(answer_back - i))


    # 비교, 같다면, 더 작은 위치 출력
    if total_cost >= total_cost_back:
        print(answer_back)
    else:
        print(answer)



else:
    total = 0
    answer = 0
    for i in arr:
        temp = dic[i]
        total += temp

        # 중간지점이 포함된 영역이면, 해당 마을 저장
        if total > half:
            answer = i
            break

    print(answer)




