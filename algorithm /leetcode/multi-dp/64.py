

class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0]*n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                # 위, 왼쪽 모두 가능한경우
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

                elif i == 0:
                    if j == 0:
                        continue
                    #  옆만 가능
                    dp[i][j] = dp[i][j-1] + grid[i][j]

                elif j == 0:
                    if i == 0:
                        continue
                    dp[i][j] = dp[i-1][j] + grid[i][j]
        return dp[-1][-1]

a = Solution()
grid =  [[1,2,3],[4,5,6]]
print(a.minPathSum(grid))