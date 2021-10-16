

n = int(input())

dp = [0] * n



next_2, next_3, next_5 = 2,3,5

index_2 =  index_3 = index_5 = 0

for i in range(1,n):
    dp[i] = min(next_2,next_3,next_5)

    if dp[i] == next_2:
        index_2 +=1
        next_2 = dp[index_2] * 2

    if dp[i] == next_3 :
        index_3 += 1
        next_3 = dp[index_3] * 3

    if dp[i] == next_5:
        index_5 += 1
        next_5 = dp[index_5] * 5

print(dp[n-1])








# 시간복잡도 실패 버전
#
# def check(num):
#
#     if num%2 !=0 and num%3 !=0 and num%5 !=0:
#
#         return False
#     else:
#
#         new_num = num
#         while True:
#
#             if new_num%2 ==0:
#                 new_num = new_num//2
#
#             if new_num%3 ==0:
#                 new_num = new_num//3
#             if new_num%5 ==0:
#                  new_num= new_num//5
#
#             if new_num == 1:
#                 return num
#
#             if new_num%2 !=0 and new_num%3 !=0 and new_num%5 !=0:
#                 return False
#
#
#
# for i in range(n-1):
#     next = dp[-1] + 1
#
#     while True:
#         if check(next) == False:
#             next +=1
#             continue
#         else:
#             dp.append(check(next))
#             break
#
#
#
#
#
# print(dp[n-1])