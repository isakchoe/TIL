#
# def solution(info, query):
#
#     # 효율성 제로!!
#     answer = []
#
#     # 질문 탐색하면서
#     for q in query:
#         count = 0
#         temp = q.split()
#         #  조건 담기
#         blank = []
#
#         lang = temp[0]
#         if lang != "-":
#             blank.append(lang)
#         job = temp[2]
#         if job !="-":
#             blank.append(job)
#         exp = temp[4]
#         if exp !="-":
#             blank.append(exp)
#         food = temp[6]
#         if food !="-":
#             blank.append(food)
#         score = int(temp[7])
#
#         # 지원자 탐색
#         for i in info:
#             parse = i.split()
#             c = 0
#             # 조건 모두 만족하는지 확인
#             for j in range(len(blank)):
#                 if blank[j] not in parse:
#                     c += 1
#                     break
#             # 모두 만족하면 스코어 확인
#             if c == 0:
#                 if int(parse[-1]) >= score:
#                     count += 1
#             else:
#                 continue
#
#         answer.append(count)
#
#     return answer
#

#
# from bisect import bisect_left, bisect_right
#
# def solution(info, query):
# #     dic 이용,
# #   이분탐색!!
# #  lower bound!! 새로운 개념 (이분탐색에서 찾고자 하는 값 이상이 처음 시작하는 인덱스! )
#
#     dic = {}
#
#     # 탐색하면서 dic 세팅
#     for i in info:
#         temp = i.split()
#
#         lang = temp[0]
#         job = temp[1]
#         exp = temp[2]
#         food = temp[3]
#         score = int(temp[4])
#
#         # 완전체
#         if (lang + job + exp+food) not in dic:
#             dic[lang+job+exp+food] = [score]
#         else:
#             dic[lang+job+exp+food].append(score)
#
# #        1개씩
#         if ('-' + job + exp+ food) not in dic:
#             dic['-'+job+exp+food] = [score]
#         else:
#             dic['-'+job+exp+food].append(score)
#
#         if (lang + '-' + exp+ food) not in dic:
#             dic[lang+'-'+exp+food] = [score]
#         else:
#             dic[lang + '-' + exp + food].append(score)
#
#         if (lang + job + '-'+ food) not in dic:
#             dic[lang+job+'-'+food] = [score]
#         else:
#             dic[lang+job+'-'+food].append(score)
#
#         if (lang + job + exp+ '-') not in dic:
#             dic[lang+job+exp+'-'] = [score]
#         else:
#             dic[lang+job+exp+'-'].append(score)
#
# #         2개씩
#         if ('-' + '-' + exp+ food) not in dic:
#             dic['-'+'-'+exp+food] = [score]
#         else:
#             dic['-'+'-'+exp+food].append(score)
#
#         if ('-' + job + '-'+ food) not in dic:
#             dic['-'+job+'-'+food] = [score]
#         else:
#             dic['-'+job+'-'+food].append(score)
#
#         if ('-' + job + exp+ '-') not in dic:
#             dic['-'+job+exp+'-'] = [score]
#         else:
#             dic['-'+job+exp+'-'].append(score)
#
#         if (lang + '-' + '-'+ food) not in dic:
#             dic[lang+'-'+'-'+food] = [score]
#         else:
#             dic[lang+'-'+'-'+food].append(score)
#
#         if (lang + '-' + exp+ '-') not in dic:
#             dic[lang+'-'+exp+'-'] = [score]
#         else:
#             dic[lang+'-'+exp+'-'].append(score)
#
#         if (lang + job + '-'+ '-') not in dic:
#             dic[lang+job+'-'+'-'] = [score]
#         else:
#             dic[lang+job+'-'+'-'].append(score)
#
# #         3개씩
#
#         if ('-' + '-' + '-'+ food) not in dic:
#             dic['-'+'-'+'-'+food] = [score]
#         else:
#             dic['-'+'-'+'-'+food].append(score)
#
#         if ('-' + '-' + exp+ '-') not in dic:
#             dic['-'+'-'+exp+'-'] = [score]
#         else:
#             dic['-'+'-'+exp+'-'].append(score)
#
#         if ('-' + job + '-'+ '-') not in dic:
#             dic['-'+job+'-'+'-'] = [score]
#         else:
#             dic['-'+job+'-'+'-'].append(score)
#
#         if (lang + '-' + '-'+ '-') not in dic:
#             dic[lang+'-'+'-'+'-'] = [score]
#         else:
#             dic[lang+'-'+'-'+'-'].append(score)
#
# #         4개
#         if ('----') not in dic:
#             dic['----'] = [score]
#         else:
#             dic['----'].append(score)
#
#
#
#     for key,values in dic.items():
#         l = values
#         l.sort()
#
#
#     answer = []
#
# #   질문 탐색
#
#     for q in query:
#         temp = q.split()
#
#         lang = temp[0]
#         job = temp[2]
#         exp = temp[4]
#         food = temp[6]
#         score = int(temp[7])
#
#         # dic 에 없는 경우
#         if lang+job+exp+food not in dic:
#             answer.append(0)
#             continue
#
#
#         # 리스트
#         t_list = dic.setdefault(lang+job+exp+food, [])
#
#         # 이분탐색!!
#         # lower bound
#
#         # 시작 위치
#         index = bisect_left(t_list,score)
#
#         # 개수
#         # 없는 경우
#         if index >= len(t_list):
#             answer.append(0)
#         #  있는경우
#         else:
#             total = len(t_list) - index
#             answer.append(total)
#
#
#     return answer

from bisect import bisect_left

def solution(info, query):

    dic ={}

    for i in info:
        temp = i.split()

        lang = temp[0]
        job = temp[1]
        exp = temp[2]
        food = temp[3]
        score = int(temp[4])

        for a in [lang,'-']:
            for b in [job,'-']:
                for c in [exp, '-']:
                    for d in [food, '-']:
                        l = dic.setdefault(a+b+c+d, [])
                        l.append(score)

#     dic 정렬
    for key in dic:
        dic[key].sort()

    answer = []

    for q in query:
        temp = q.split()

        lang = temp[0]
        job = temp[2]
        exp = temp[4]
        food = temp[6]
        score = int(temp[7])

        if lang+job+exp+food not in dic:
            answer.append(0)
            continue

        l = dic[lang+job+exp+food]

#       리스트 이분탐섹

        index = bisect_left(l, score)

        if index >= len(l):
            answer.append(0)
        else:
            total = len(l) - index
            answer.append(total)


    return answer










# 교훈!!
#  딕셔너리 문법, 이진탐색 활용
#  딕셔너리 초기값 세팅 간단히하기!
#  이진탐색 --> lower bound, upper bound ===> bisect_left, bisect_right 단순히 개수세는개 아니다













