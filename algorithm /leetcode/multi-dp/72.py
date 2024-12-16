

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0

        n = len(word1)
        m = len(word2)

        dp = [[0] * (m+1) for _ in range(n+1)]

        # delete
        for i in range(n+1):
            dp[i][0] = i

        # insert
        for j in range(m+1):
            dp[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1]+ 1, dp[i-1][j] +1, dp[i-1][j-1] +1)
        return dp[n][m]



a = Solution()
word1 = ""
word2 = "a"
print(a.minDistance(word1, word2))

















