#
# from _collections import deque
#
# # 입력받기
# n = int(input())
#
# data = list(map(int, input().split()))
#
# oper = list(map(int, input().split()))
#
#
# q = deque()
# # 인덱스, 계산합,  연산자리스트
# q.append([0, data[0], oper])
#
# result = []
#
#
# while q:
#     idx, now, oper = q.popleft()
#
#
#     # 계산 완료한경우 삽입
#     if idx == len(data) - 1:
#         result.append(now)
#         continue
#
#     # 덧셈
#     if oper[0] != 0:
#         temp = now + data[idx+1]
#         # 연산자 리스트 복사
#         temp_oper = [0] * 4
#         for i in range(4):
#             temp_oper[i] = oper[i]
#         # 횟수 감소
#         temp_oper[0] -= 1
#         # 삽입
#         q.append([idx+1, temp, temp_oper])
#
#     # 뺄셈
#     if oper[1] != 0:
#         temp = now - data[idx + 1]
#
#         temp2_oper = [0] * 4
#         for i in range(4):
#             temp2_oper[i] = oper[i]
#
#         temp2_oper[1] -= 1
#         q.append([idx + 1, temp, temp2_oper])
#
#
#     # 곱셈
#     if oper[2] != 0:
#         temp = now * data[idx + 1]
#
#         temp3_oper = [0] * 4
#         for i in range(4):
#             temp3_oper[i] = oper[i]
#
#         temp3_oper[2] -= 1
#         q.append([idx + 1, temp, temp3_oper])
#
#     # 나눗셈
#     if oper[3] != 0:
#         # 음수를 나눌경우
#         if now < 0:
#             temp = -(-now // data[idx + 1])
#         # 양수일 경우
#         else:
#             temp = now // data[idx + 1]
#
#         temp4_oper = [0] * 4
#         for i in range(4):
#             temp4_oper[i] = oper[i]
#
#         temp4_oper[3] -= 1
#         q.append([idx + 1, temp, temp4_oper])
#
#
#
#
# max_result = max(result)
# min_result = min(result)
#
# # 출력
# print(max_result)
# print(min_result)


# dfs 풀이

n = int(input())
data = list(map(int, input().split()))

add, sub, multi, divi = map(int, input().split())

min_result = int(1e9)
max_result = -int(1e9)

def dfs(idx, total):

    # 글로벌이 핵심!! --> 재귀의 포인트
    global min_result, max_result, add, sub, multi, divi

    if idx == n:
        min_result = min(min_result, total)
        max_result = max(max_result, total)

    else:
        if add > 0:
            # 먼저 감소하고, 재귀
            add -= 1
            dfs(idx +1, total + data[idx])
            add += 1

        if sub > 0:
            # 먼저 감소하고, 재귀
            sub -= 1
            dfs(idx +1, total - data[idx])
            sub += 1

        if multi > 0:
            # 먼저 감소하고, 재귀
            multi -= 1
            dfs(idx +1, total * data[idx])
            multi += 1

        if divi>0:
            divi -= 1
            dfs(idx + 1, int(total / data[idx]))
            divi += 1

dfs(1, data[0])



print(max_result)
print(min_result)
