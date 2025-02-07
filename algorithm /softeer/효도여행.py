

import sys
sys.setrecursionlimit(5000)

n, m = map(int, input().split())
S = input()

ad_list = [[] for _ in range(n)]

for _ in range(n-1):
    a, b, value = input().split()
    a = int(a)-1
    b = int(b)-1

    # 양방향
    ad_list[a].append([b,value])
    ad_list[b].append([a,value])


start_list = ad_list[0]
visited = [False] * n

answer = 0


def longest_common_subsequence(str1, str2):
    len1, len2 = len(str1), len(str2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len1][len2]

def dfs(arr, sum_route):
    global answer

    for next_node, value in arr:
        if not visited[next_node]:
            visited[next_node] = True
            sum_route.append(value)

            next_next = ad_list[next_node]

            if len(next_next) == 1:
                result = ''.join(sum_route)
                if len(result) > answer:
                    answer = max(answer, longest_common_subsequence(result, S))
            else:
                dfs(next_next, sum_route)

            # backtrack
            visited[next_node] = False
            sum_route.pop()


visited[0] = True
dfs(start_list, [])


print(answer)

