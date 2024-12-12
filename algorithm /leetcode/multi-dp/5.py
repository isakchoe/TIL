

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # i 번째를 꼭 포함해서 펠린드롬..
        dp = [1] * n
        answer = s[0]

        for i in range(1, n):
            for j in range(i):
                if s[j] == s[i]:
                    if self.check_palindrome(s[j:i+1]):
                        temp = i-j+1
                        
                        if temp > dp[i-1]:
                            dp[i] = temp
                            answer = s[j:i+1]
                        break
            # 펠린드롬 되는 경우 하나도 없는 경우도 고려..
            dp[i] = max(dp[i], dp[i-1])
        return answer


    def check_palindrome(self, s):
        n = len(s)
        half = n // 2

        for i in range(half):
            if s[i] != s[-(i+1)]:
                return False
        return True


a = Solution()
s = "abadd"
print(a.longestPalindrome(s))