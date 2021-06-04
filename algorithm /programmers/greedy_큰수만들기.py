
#  스택을 잘못사용 !!!

# def solution(number, k):
#     # stack 만들기
#     # 앞에서부터 number 순차 탐색하면서 스택에 쌓기
#     # 탑보다 작으면 해당 수 제거 count ++
#     # 탑보다 크면 pop, ==> 해당 수 제거, count ++ ,   쌇기
#     # count ==k  종결! return count !
#
#
#
#     stack = []
#     stack.append(number[0])
#
#     # 숫자리스트
#     n_list = []
#     for i in range(len(number)):
#         n_list.append(number[i])
#
#     count = 0
#
#     # 탐색
#     for i in range(1, len(number)):
#         # 탑보다 작은 경우
#         if stack[-1] > number[i]:
#             n_list.remove(number[i])
#             count += 1
#
#         else:
#             # 스택 비우기
#             while len(stack) !=0:
#                 n_list.remove(stack.pop())
#                 count += 1
#                 if count == k:
#                     break
#
#             stack.append(number[i])
#
#         if count == k:
#             break
#
#     answer = "".join(n_list)
#
#     return answer




# 시간 복잡도 터져!

# def solution(number, k):
#     #  맨끝에서 자리수 잡고, 앞으로 탐색하면서 범위 늘리기
#     #  제일 앞자리랑 비교해서 크면 삽입, 배열내에서  앞 인덱스보다 작으면서 뒤 인덱스보다 작은 부분 제거!!
#     # 크지 않으면 스킵, 다음꺼랑 비교
#
#
#     n = len(number)
#
#     # 스택에 담기
#     stack = []
#     for i in range(n-1, k-1, -1):
#         stack.append(int(number[i]))
#
#     # 거꾸로 탐색
#     for i in range(k-1, -1, -1):
#         if int(number[i]) >= stack[-1]:
#             # 삽입
#             stack.append(int(number[i]))
#             #꺽이는부분삭제
#             index = 0
#             for j in range(len(stack)-2, -1, -1):
#                 if stack[j] > stack[j+1]:
#                     index = j+1
#                     break
#     #         꺽이는 부분 없으면 최소 값 삭제
#             del stack [index]
#
#
#     answer = ""
#
#     for i in range(len(stack)):
#         answer += str(stack.pop())
#
#     return answer
#



def solution(number, k):
    # 스택만들기
    # number 순차탐색
    # 탑보다 작으면 쌓기
    # 탑보다 크면 pop 하고  count ++ ,   비교 ==> 위 과정 반복
    # 중간에 count == k 이면 break ===> 예외가 있디!! 처음부터 내림차순이면 k는 계속 0 ,  스택으로 문자열 만들어서 리턴!

    # 스택
    stack = []
    stack.append(int(number[0]))

    count = 0
    m = len(number) - k

    #탐색
    for i in range(1, len(number)):
        now = int(number[i])
        # 카운트 다 채우면, 그 뒤는 그냥 연결
        if count == k:
            stack.append(now)
            continue

        # 탑보다 작은경우
        if now <= stack[-1]:
            stack.append(now)
        # 탑보다 큰경우
        else:
            while len(stack) != 0:
                stack.pop()
                count += 1
                # 스택이 비었거나, 탑보다 작다면 삽입
                if len(stack) == 0  or stack[-1] >= now:
                    stack.append(now)
                    break
                # 카운트 == k 이면, 그냥 삽입 (주의!!)
                if count == k:
                    stack.append(now)
                    break


    answer =  ""

    for i in range(m):
        answer += str(stack[i])

    return answer


