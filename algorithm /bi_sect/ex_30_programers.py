
from bisect import bisect_left, bisect_right

#
# def check(a ,b):
#
#     length = len(a)
#
#     if length == len(b):
#         for i in range(length):
#             if a[i] == b[i] or b[i] = ="?":
#                 continue
#             else:
#                 return False
#
#         return True
#     else:
#         return False
#
#
# def compari(s1 ,s2):
#     blank =[s1, s2]
#     blank.sort()
#
#     return blank[1]
#
#
# def count_by_range(arr, left, right):
#     left_index = bisect_left(arr, left)
#     right_index = bisect_right(arr, right)
#     return right_index - left_index
#
#
# def b_search(arr, start, end, target):
#     if start > end:
#         return None
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if check(arr[mid], target):
#             if mid == 0 or check(arr[mid - 1], target) == False:
#                 return mid
#             elif check(arr[mid - 1], target):
#                 end = mid - 1
#             else:
#                 start = mid + 1
#
#         else:
#             if compari(arr[mid], target) == target:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#
#     return None
#
#
# def r_search(arr, start, end, target):
#     if start > end:
#         return None
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if check(arr[mid], target):
#             if mid == len(arr) - 1 or check(arr[mid + 1], target) == False:
#                 return mid
#             elif check(arr[mid + 1], target):
#                 start = mid + 1
#             else:
#                 end = mid - 1
#
#         else:
#             if compari(arr[mid], target) == target:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#
#     return None
#
#
# def solution(words, queries):
#     words.sort()
#
#     answer = []
#
#     for i in queries:
#         left_index = b_search(words, 0, len(words) - 1, i)
#
#         if left_index == None:
#             answer.append(0)
#             continue
#         r_index = r_search(words, 0, len(words) - 1, i)
#
#         result = r_index - left_index + 1
#
#         answer.append(result)
#
#     return answer


def count_by_range(arr,l,r):
    left_index = bisect_left(arr,l)
    right_index = bisect_right(arr,r)

    return right_index - left_index

array = [ [] for _ in range(10001)]

reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []

    for word in words:
        array[len(word)].append(word)

        # 단어 뒤집어서 삽입
        reversed_array[len(word)].append(word[::-1])

    # 정렬
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0]!= "?":
            res = count_by_range(array[len(q)], q.replace("?", "a"), q.replace("?", 'z'))
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace("?","a"), q[::-1].replace("?", "z"))

        answer.append(res)

    return answer
