

# 그리디?
# 단위시간당 가성비 구해서, 최대 먼저 공부
#
# 그리디 실패 ==> dp, 배낭알고리즘 학습!!



# n, k = map(int, input().split())
#
# subjects = []
#
# for _ in range(k):
#     score, time = map(int, input().split())
#
#     # 시간당 중요도
#     score_per_time = score/time
#
#     subjects.append([score_per_time, score,time])
#
# # 내림차순 정렬
# subjects.sort(key=lambda x: -x[0])
# print(subjects)
#
# total = 0
#
# for subject in subjects:
#     score_per_time, score, time = subject
#
#     # 수강가능하면
#     if time <= n:
#         n -= time
#         total += score
#
# print(total)




import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0]*(n+1) for _ in range(k+1)]

arr = [[0,0]]

for _ in range(k):
    value, time = map(int, input().split())
    arr.append([value, time])

# 배낭알고리즘
for i in range(1,k+1):
    for j in range(1, n+1):
        # 수강 가능
        if arr[i][1] <= j:
            dp[i][j] = max(dp[i-1][j], arr[i][0] + dp[i-1][j - arr[i][1]])
        else:
            dp[i][j] = dp[i-1][j]

# 출력
print(dp[-1][-1])

