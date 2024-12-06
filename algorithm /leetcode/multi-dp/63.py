


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [ [0]*n for _ in range(m)]
        dp[0][0] = 1


        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                if i == 0:
                    # can go
                    if obstacleGrid[i][j-1] == 0:
                        dp[i][j] += dp[i][j-1]

                elif j == 0:
                    if obstacleGrid[i-1][j] == 0:
                        dp[i][j] += dp[i-1][j]

                else:
                    if obstacleGrid[i][j-1] == 0:
                        dp[i][j] += dp[i][j-1]

                    if obstacleGrid[i-1][j] == 0:
                        dp[i][j] += dp[i-1][j]
        return dp[-1][-1]

a = Solution()
obstacleGrid =  [[0,0],[0,1]]
print(a.uniquePathsWithObstacles(obstacleGrid))