
# 1. 주어진 문자가 회문이 아닌경우 ==> 문자열 길이가 답
# 2. 회문인 경우
#         1) 전체가 zzzz 같은 경우  return -1
#         2)  abcba    ==> 전체길이 - 1


def is_pal(str):
    for i in range(len(str)//2):
        if str[i] != str[-(i+1)]:
            return False
    return True


string = input()

# 회문판별

# 주어진 문자열이 회문이면
if is_pal(string):
    # 처음부터 마지막직전 요소까지도 회문이면 zzzzz 같은 모양
    if is_pal(string[:-1]):
        print(-1)
    else:
        print(len(string)-1)
else:
    print(len(string))









# ------------ 실패버전 -----------#  시간복잡도 n * logn   완탐

# from collections import deque
#
#
# string = input()
#
# # log N 복잡도
# def is_pal(arr):
#     for i in range(len(arr)//2):
#         if arr[i] != arr[-(i+1)]:
#             return False
#     return True
#
# # 큰거부터 작은범위로 탐색
#
# n = len(string)
#
# answer = -1
#
#
# # 스택과 큐 사용
# #  n * log n   n = 50만
#
# stack = list(string)
# q = deque(list(string))
#
#
# for i in range(n):
#
#     if is_pal(stack) is not True or is_pal(q) is not True:
#         answer = n -i
#         break
#
#     # 범위 줄이기
#     stack.pop()
#     q.popleft()
#
# print(answer)


