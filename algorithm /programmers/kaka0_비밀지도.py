import time
#
# def make(num):
#     temp = ""
#     while num != 1:
#         rest = num % 2
#         num = num // 2
#         temp = str(rest) + temp
#
#     temp = "1" + temp
#     return temp
#
#
# def solution(n, arr1, arr2):
#     t1 = time.time()
#     arr1 = list(map(make, arr1))
#     arr2 = list(map(make, arr2))
#
#     for i in range(n):
#         while len(arr1[i]) != n:
#             arr1[i] = "0" + arr1[i]
#         while len(arr2[i]) != n:
#             arr2[i] = "0" + arr2[i]
#
#     new_arr = []
#
#     for i in range(n):
#         up = arr1[i]
#         down = arr2[i]
#         temp = ""
#         for j in range(n):
#             if up[j] == "0" and down[j] == "0":
#                 temp += " "
#             else:
#                 temp += "#"
#         new_arr.append(temp)
#     t2 = time.time()
#     print(t2-t1)
#     return new_arr





def solution(n, arr1, arr2):

    t1 =time.time()
    # 2진법 변환
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:]
        while len(arr1[i]) != n:
            arr1[i] = "0" + arr1[i]

        arr2[i] = bin(arr2[i])[2:]
        while len(arr2[i]) != n:
            arr2[i] = "0" + arr2[i]


    answer = []
#     합치기
    for i in range(n):
        up = arr1[i]
        down = arr2[i]

        temp = ""

        for j in range(n):
            if up[j] == "0" and down[j] == "0":
                temp += " "
            else:
                temp += "#"

        answer.append(temp)
    t2 = time.time()
    print(t2-t1)
    return answer






n = 16
arr1 = [2**16-1]*16
arr2 =  [2**16-1]*16
if __name__ == '__main__':

    print(solution(n,arr1,arr2))