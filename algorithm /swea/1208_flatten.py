
import sys
sys.stdin = open("input.txt")


# 최대값 인덱스 구하는 함수
def max_index(list):
    max_value = list[0]
    index = 0
    for i in range(len(list)):
        if list[i] > max_value:
            max_value = list[i]
            index = i
    return index

# 최소값 인덱스 구하는 함수
def min_index(list):
    min_value = list[0]
    index = 0
    for i in range(len(list)):
        if list[i] < min_value:
            min_value = list[i]
            index = i
    return index



# 입력
for tc in range(1,11):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        max_i = max_index(arr)
        min_i = min_index(arr)

        # 평탄화 마무리
        if max_i == min_i:
            break
        elif max(arr) - min(arr) == 1:
            break
        # 평탄화 아니면
        else:
            # dump
            arr[max_i] -= 1
            arr[min_i] += 1


    answer = max(arr) - min(arr)
    print(f"#{tc} {answer}")
