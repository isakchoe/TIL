

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2, 3]

        if n > 3:
            for i in range(4, n+1):
                temp = dp[i-1] + dp[i-2]
                dp.append(temp)

        return dp[n]

a = Solution()
n = 4
print(a.climbStairs(n))
