

class Solution:
    def minimumTotal(self, triangle: [[int]]) -> int:
        dp = [triangle[0]]

        n = len(triangle)

        if n > 1:
            for i in range(1, n):
                temp = []
                for j in range(len(triangle[i])):

                    # 처음, 끝
                    if j == 0:
                        min_value = dp[i - 1][j]
                    elif j == i:
                        min_value = dp[i-1][-1]
                    else:
                        minus = dp[i-1][j-1]
                        current = dp[i-1][j]
                        min_value = min(minus, current)
                    temp.append(min_value+triangle[i][j])
                dp.append(temp)

        return min(dp[n-1])


a = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(a.minimumTotal(triangle))


